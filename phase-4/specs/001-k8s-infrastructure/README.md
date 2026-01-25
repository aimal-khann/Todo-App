# Todo App - Local Kubernetes Infrastructure (Phase IV)

This document describes the Kubernetes-based deployment of the Todo App using Helm charts.

## Architecture Overview

The application consists of three main components deployed on Kubernetes:

1. **Frontend**: Next.js application serving the user interface
2. **Backend**: FastAPI application providing the API
3. **Database**: PostgreSQL database for data persistence

## Prerequisites

- Docker
- Minikube
- Helm 3+
- kubectl

## Deployment

### 1. Start Minikube

```bash
minikube start --cpus=4 --memory=8192 --disk-size=20g
```

### 2. Set Docker Environment

```bash
eval $(minikube -p minikube docker-env)
```

### 3. Build Docker Images

```bash
# Build backend
cd backend
docker build -t todo-backend:v1 .
cd ..

# Build frontend
cd frontend
docker build -t todo-frontend:v1 .
cd ..
```

### 4. Deploy with Helm

```bash
helm install todo-app ./k8s/helm/todo-app --wait
```

### 5. Access the Application

```bash
# Get frontend URL
minikube service todo-frontend --url
```

## Configuration

The Helm chart is configurable via the `values.yaml` file. Key configuration parameters:

- `frontend.replicaCount`: Number of frontend replicas
- `backend.replicaCount`: Number of backend replicas
- `postgresql.enabled`: Whether to deploy PostgreSQL
- `secrets`: Contains sensitive configuration values
- `configMaps`: Contains non-sensitive configuration values

## Security

- Secrets are stored using Kubernetes Secrets
- Network policies restrict traffic between services
- Health checks ensure service availability

## Persistence

PostgreSQL data is persisted using PersistentVolumeClaims to ensure data durability across pod restarts.

## Troubleshooting

Use `kubectl-ai` for intelligent troubleshooting:

```bash
kubectl-ai explain pod <pod-name>
kubectl-ai logs <pod-name>
```

Analyze cluster resources with `kagent`:

```bash
kagent analyze
kagent resources
```

## Scaling

Scale deployments using kubectl:

```bash
kubectl scale deployment todo-frontend --replicas=3
kubectl scale deployment todo-backend --replicas=2
```