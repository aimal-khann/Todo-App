<!--
SYNC IMPACT REPORT
Version change: 1.0.0 → 2.0.0
Modified principles: Frontend Isolation → Full-Stack Integration, Mock-First Architecture → Type Parity & Stateless Architecture
Added sections: Backend Technology Stack, Full-Stack Architecture Rules, Full-Stack Coding Standards
Removed sections: Frontend Isolation, Mock-First Architecture principles
Templates requiring updates:
  - ✅ plan-template.md (will reference new constitution in Constitution Check)
  - ✅ spec-template.md (aligns with full-stack requirements)
  - ✅ tasks-template.md (aligns with full-stack requirements)
Follow-up TODOs: None
-->

# Evolution of Todo (Phase II) - Full Stack Implementation Constitution

## Core Principles

### Full-Stack Integration
We are now building the Backend. The frontend must eventually consume real APIs, removing mock data. The architecture must support both frontend and backend development with proper separation of concerns.

### Type Parity
TypeScript interfaces (Frontend) and Pydantic models (Backend) must stay synchronized. Data contracts between frontend and backend must be consistent and validated.

### Stateless Architecture
The backend must be stateless, verifying JWT tokens on every protected request. No server-side session storage, relying on token-based authentication.

### Agentic Workflow
Follow the cycle: Specify → Plan → Tasks → Implement.

### Modern Technology Stack
Frontend: Next.js 16+, TypeScript (Strict Mode), Tailwind CSS, Shadcn/UI, Lucide React, Framer Motion, React Query, Zustand, Better Auth, Zod, and React Hook Form. Backend: FastAPI, Python 3.10+, Neon Serverless PostgreSQL, SQLModel, python-jose, and Alembic.

### Cyberpunk Design Aesthetic
Use a 'Cyberpunk/Modern' aesthetic. Dark mode by default with high-contrast accents. Implement Atomic Design and mobile-first responsive design.

## Technology & Architecture Constraints

### Folder Structure
- `/frontend`: Next.js code (Keep existing).
- `/backend`: Python FastAPI service (New).

### API Standards
RESTful endpoints returning JSON. Snake_case for Python, camelCase for JSON responses. All endpoints must follow consistent naming conventions.

### Database
All tables must have `created_at` and `updated_at` timestamps. Use Neon Serverless PostgreSQL with SQLModel as the ORM. Implement proper database migration strategies with Alembic.

### Security
Never commit `.env` files. Use environment variables for DB URLs and secret keys. All authentication tokens must be properly verified using python-jose for JWT decoding.

## Development Workflow
Follow the agentic workflow: Specify → Plan → Tasks → Implement. Use strict type hints in Python and TypeScript. Implement proper error handling on both frontend and backend. Replace `MockAuthService` with actual API calls to the backend using `Axios` or `Fetch`. Modular routers should be implemented in `/api/v1/...` pattern.

## Governance
All code must comply with the principles above. Full-stack implementations must include both frontend and backend components. Code reviews must verify compliance with the technology stack and design requirements. All components must follow Atomic Design principles on the frontend and modular design on the backend. Type parity between frontend interfaces and backend models must be maintained.

**Version**: 2.0.0 | **Ratified**: 2026-01-02 | **Last Amended**: 2026-01-02