<!--
SYNC IMPACT REPORT
Version change: 4.0.0 → 5.0.0
Modified principles: MCP-Native Backend Architecture → Cloud-Native Container-First Architecture, Synchronous Database Operations → Statelessness and Externalized State
Added sections: Container-First Philosophy, Kubernetes Orchestration, Infrastructure as Code with Helm, AIOps Workflow Requirements, Configuration Management, Observability Standards
Removed sections: MCP-Native Architecture (replaced with cloud-native focus)
Templates requiring updates:
  - ✅ plan-template.md (updated to reflect cloud-native requirements)
  - ✅ spec-template.md (aligns with container-first approach)
  - ✅ tasks-template.md (includes cloud-native deployment tasks)
  - ✅ governance procedures updated for cloud-native compliance
Follow-up TODOs: None
-->

# Cloud-Native & AIOps Constitution

## Core Principles

### Container-First Philosophy
All services (Frontend, Backend) MUST be containerized using Docker. **NO bare-metal deployments:** All functionality runs inside containerized environments managed by Kubernetes. Docker AI (Gordon) MUST be used to generate and optimize Dockerfiles for all services.

### Kubernetes Orchestration
Kubernetes (Minikube) is the SOLE source of truth for runtime orchestration. All deployments, scaling, and lifecycle management must occur through Kubernetes primitives. kubectl-ai MUST be used to generate initial K8s manifests and troubleshoot deployment errors.

### Infrastructure as Code (IaC) with Helm
All infrastructure (Deployments, Services, ConfigMaps, Secrets) MUST be defined via **Helm Charts**. NO ad-hoc `kubectl run` commands allowed for permanent infrastructure. Helm provides versioning, templating, and release management for all Kubernetes resources.

### AIOps Workflow Requirements
- **Docker AI (Gordon):** MUST be used to generate and optimize Dockerfiles
- **kubectl-ai:** MUST be used to generate initial K8s manifests and troubleshoot deployment errors
- **Kagent:** MUST be used for cluster health analysis and resource optimization validation

### Statelessness and Externalized State
Application pods MUST be stateless. All persistent state MUST be externalized to PostgreSQL or other external storage systems. No application-level persistence within containers is permitted to ensure scalability and reliability.

### Configuration Management
Environment variables MUST be mapped via K8s ConfigMaps and Secrets. NO hardcoded configurations or environment-specific files. All configuration must be externalized and managed through Kubernetes native objects.

### Observability Standards
All pods MUST have basic liveness and readiness probes configured. Applications must emit structured logs and metrics compatible with Kubernetes monitoring stacks. Health checks must follow Kubernetes best practices.

### Service Communication
Services must communicate through Kubernetes Services with proper networking configurations. Frontend → Backend → DB communication must be secured and load-balanced through Kubernetes native service discovery mechanisms.

### Zero Manual YAML Policy
NO manual YAML writing for Kubernetes manifests. All Kubernetes resources must be AI-generated using approved AIOps tools (kubectl-ai, Docker AI). Manual editing is prohibited except for emergency troubleshooting.

## Technology & Architecture Constraints

### Tech Stack Mandate
- Containerization: Docker with optimized images via Docker AI (Gordon)
- Orchestration: Kubernetes (Minikube for development)
- IaC: Helm Charts for all infrastructure definitions
- Monitoring: Kubernetes-native observability stack
- AIOps Tools: Docker AI, kubectl-ai, Kagent for cluster analysis

### Deployment Requirements
- All deployments MUST follow the container-first approach
- Images MUST be built with AI-optimized Dockerfiles
- Deployments MUST include proper resource limits and requests
- All services MUST have health checks configured
- Networking MUST be configured through Kubernetes Services

### Security Requirements
- Pod security policies MUST be enforced
- Network policies SHOULD restrict inter-service communication
- Secrets MUST be managed through Kubernetes Secret objects
- RBAC rules MUST be properly configured for all components
- Container images MUST be scanned for vulnerabilities

### Resource Management
- Resource quotas MUST be defined for all namespaces
- Horizontal Pod Autoscaling SHOULD be configured where appropriate
- Storage MUST be provisioned through PersistentVolumeClaims
- Cluster resources MUST be monitored using Kagent for optimization

## Development Workflow

Follow the agentic workflow: Specify → Plan → Tasks → Implement. All implementations must comply with cloud-native principles. Use Docker AI for container optimization, kubectl-ai for manifest generation, and Kagent for cluster analysis. Implement proper health checks, externalized state management, and configuration through ConfigMaps/Secrets. All infrastructure must be defined as Helm charts with no manual YAML manipulation.

## Governance

All code and infrastructure must comply with the Cloud-Native & AIOps principles. Deployments must follow container-first philosophy with proper Kubernetes orchestration. Helm Charts must be used for all infrastructure definitions. AIOps tools must be utilized for Docker optimization, manifest generation, and cluster analysis. Applications must be stateless with externalized persistence. Configuration must be managed through Kubernetes native objects. All deployments must include proper observability with health checks and structured logging.

**Version**: 5.0.0 | **Ratified**: 2026-01-10 | **Last Amended**: 2026-01-24