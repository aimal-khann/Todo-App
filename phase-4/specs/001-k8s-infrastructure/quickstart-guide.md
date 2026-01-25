# Quick Start Guide: Todo App on Kubernetes

## Overview
This guide provides a quick way to get the Todo App running on Kubernetes using Minikube and Helm.

## Prerequisites
- Docker installed and running
- Minikube installed
- Helm 3+ installed
- kubectl installed

## Quick Deployment Steps

### 1. Start Minikube
```bash
minikube start --cpus=4 --memory=8192 --disk-size=20g
```

### 2. Set Docker Environment
```bash
eval $(minikube -p minikube docker-env)
```

### 3. Build Application Images
```bash
# Build backend image
cd backend
docker build -t todo-backend:v1 .
cd ..

# Build frontend image
cd frontend
docker build -t todo-frontend:v1 .
cd ..
```

### 4. Deploy to Kubernetes
```bash
# Install the Helm chart
helm install todo-app ./k8s/helm/todo-app --wait
```

### 5. Verify Deployment
```bash
# Check if all pods are running
kubectl get pods

# Check services
kubectl get services

# Wait for all pods to be ready
kubectl wait --for=condition=ready pod -l app=backend --timeout=300s
kubectl wait --for=condition=ready pod -l app=frontend --timeout=300s
kubectl wait --for=condition=ready pod -l app=postgresql --timeout=300s
```

### 6. Access the Application
```bash
# Get the frontend URL
minikube service todo-frontend --url
```

## Troubleshooting Quick Commands

### Check Pod Status
```bash
kubectl get pods
kubectl describe pod <pod-name>
kubectl logs <pod-name>
```

### Check Service Status
```bash
kubectl get services
kubectl describe service <service-name>
```

### Use kubectl-ai for Intelligent Troubleshooting
```bash
kubectl-ai explain pod <pod-name>
kubectl-ai logs <pod-name> --context
```

### Check Resource Usage
```bash
kubectl top nodes
kubectl top pods
```

## Cleanup
```bash
# Uninstall the Helm release
helm uninstall todo-app

# Stop Minikube (optional)
minikube stop
```

## Next Steps
- Customize the application using the `values.yaml` file
- Scale the application based on demand
- Monitor application health using Kubernetes dashboard
- Set up ingress for external access