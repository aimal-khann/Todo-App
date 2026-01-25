# Multi-stage Dockerfile for Next.js Frontend with standalone output
# Stage 1: Install dependencies
FROM node:20-alpine AS deps

# Install only production dependencies
WORKDIR /app
COPY package.json ./
COPY package-lock.json ./
RUN npm ci --only=production

# Stage 2: Build the application
FROM node:20-alpine AS builder

WORKDIR /app

# Copy dependencies from previous stage
COPY --from=deps /app/node_modules ./node_modules

# Copy source files
COPY . .

# Build the Next.js application
RUN npm run build

# Stage 3: Runtime environment
FROM node:20-alpine

WORKDIR /app

# Install minimal system dependencies including curl for health checks
RUN apk add --no-cache curl dumb-init

# Copy package.json for reference
COPY package.json .

# Copy node_modules from deps stage
COPY --from=deps /app/node_modules ./node_modules

# Copy the built Next.js application
COPY --from=builder /app/.next ./.next
COPY --from=builder /app/public ./public

# Expose port
EXPOSE 3000

# Health check
HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:3000/api/health || exit 1

# Use dumb-init to handle signals properly
ENTRYPOINT ["dumb-init", "--"]

# Command to run the application
CMD ["npm", "start"]