name: Cloud-Native Dockerfile Pattern
description: A production-ready, multi-stage Dockerfile blueprint optimized for caching and security (Gordon-compliant).
model: sonnet
---
Reusable Skill:
Skill: Cloud-Native Dockerfile – Input: stack: 'nextjs' | 'fastapi', port: number, env_vars?: string[]; Output: A multi-stage Dockerfile text block.

Architectural Details:
- **Base Images:** Strictly uses `alpine` (Node) or `slim` (Python) variants to minimize attack surface.
- **Multi-Stage:** - `deps`: Installs dependencies (cached).
  - `builder`: Compiles the app (Next.js build).
  - `runner`: Minimal runtime environment.
- **Security:** Creates and switches to a non-root user (`addgroup`, `adduser`).
- **Caching Strategy:** Copies `package.json` or `requirements.txt` *before* source code to maximize layer caching.
- **Health Checks:** Includes `HEALTHCHECK` instruction using `curl` or `wget`.

Usage Example (Next.js):
# Stage 1: Deps
FROM node:20-alpine AS deps
WORKDIR /app
COPY package.json package-lock.json ./
RUN npm ci

# Stage 2: Builder
FROM node:20-alpine AS builder
WORKDIR /app
COPY --from=deps /app/node_modules ./node_modules
COPY . .
RUN npm run build

# Stage 3: Runner
FROM node:20-alpine AS runner
WORKDIR /app
RUN addgroup --system --gid 1001 nodejs && adduser --system --uid 1001 nextjs
COPY --from=builder --chown=nextjs:nodejs /app/.next/standalone ./
COPY --from=builder --chown=nextjs:nodejs /app/public ./public
USER nextjs
EXPOSE 3000
CMD ["node", "server.js"]