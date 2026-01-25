---
id: "001"
title: "update-cloud-native"
stage: "constitution"
date_iso: "2026-01-24"
surface: "agent"
model: "claude-sonnet-4-5-20250929"
feature: "none"
branch: "main"
user: "user"
command: "/sp.constitution **Phase IV: Cloud-Native Mandate**"
labels: ["cloud-native", "kubernetes", "docker", "aiops"]
spec_url: "null"
ticket_url: "null"
adr_url: "null"
pr_url: "null"
---

# PHR: Update Constitution to Cloud-Native & AIOps Principles

## Command
```
/sp.constitution **Phase IV: Cloud-Native Mandate**
```

## User Input
```
**Phase IV: Cloud-Native Mandate**

Update the project constitution to adopt **Cloud-Native & AIOps Principles** for Phase 4.

**1. Deployment Philosophy:**
   - **Container-First:** All services (Frontend, Backend) must be containerized using Docker.
   - **Orchestration:** Kubernetes (Minikube) is the sole source of truth for runtime orchestration.
   - **Infrastructure as Code (IaC):** All infrastructure (Deployments, Services, ConfigMaps, Secrets) must be defined via **Helm Charts**. No ad-hoc `kubectl run` commands allowed for permanent infrastructure.

**2. AIOps Workflow (Strict Requirement):**
   - **Docker AI (Gordon):** MUST be used to generate and optimize Dockerfiles.
   - **kubectl-ai:** MUST be used to generate initial K8s manifests and troubleshoot deployment errors.
   - **Kagent:** MUST be used for cluster health analysis and resource optimization validation.

**3. Architecture Standards:**
   - **Statelessness:** Application pods must be stateless. State must be externalized (PostgreSQL).
   - **Configuration:** Environment variables must be mapped via K8s ConfigMaps and Secrets.
   - **Observability:** Pods must have basic liveness and readiness probes.

**4. Definition of Done (Phase 4):**
   - Frontend and Backend deployed as Pods in Minikube.
   - Services successfully communicating (Frontend -> Backend -> DB).
   - Application accessible via `minikube service` or Ingress.
   - Zero manual YAML writing; AI generation required.
```

## Response Summary
Updated the project constitution to adopt Cloud-Native & AIOps Principles for Phase 4. The new constitution includes:

- Container-First Philosophy requiring Docker containerization
- Kubernetes Orchestration using Minikube as the source of truth
- Infrastructure as Code with Helm Charts for all infrastructure
- AIOps Workflow Requirements mandating Docker AI, kubectl-ai, and Kagent
- Statelessness and Externalized State principles
- Configuration Management through K8s ConfigMaps and Secrets
- Observability Standards with health checks
- Zero Manual YAML Policy

Also updated the template files to align with the new constitution:
- Modified plan-template.md to include cloud-native compliance gates
- Updated tasks-template.md to include cloud-native deployment tasks
- Enhanced spec-template.md with cloud-native requirements

## Files Modified
 - .specify/memory/constitution.md
 - .specify/templates/plan-template.md
 - .specify/templates/tasks-template.md
 - .specify/templates/spec-template.md

## Outcome
Successfully updated the constitution to reflect cloud-native and AIOps principles, with all dependent templates updated to maintain consistency. The new constitution version is 5.0.0, representing a major update due to fundamental architectural changes from MCP-native to cloud-native approach.

## Evaluation
The constitution update aligns with the user's requirements for Phase IV Cloud-Native Mandate. All specified principles have been incorporated into the document, and supporting templates have been updated to enforce compliance with the new principles.