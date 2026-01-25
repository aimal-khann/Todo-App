# Quickstart Guide: Local Kubernetes Infrastructure (Phase IV)

## Overview
This guide provides step-by-step instructions to deploy the Todo App to Minikube using the completed Kubernetes infrastructure implementation.

## Prerequisites
- Docker Desktop with Kubernetes enabled OR Minikube installed
- Helm 3.x
- kubectl
- Node.js 18+ (for local development)
- Python 3.11+ (for backend development)

## Setup Instructions

### 1. Start Minikube
```bash
# Start Minikube with sufficient resources
minikube start --cpus=4 --memory=8192 --disk-size=20g

# Configure Docker to use Minikube's Docker daemon
eval $(minikube -p minikube docker-env)
```

### 2. Clone the Repository
```bash
git clone <repository-url>
cd <repository-directory>
git checkout 001-k8s-infrastructure
```

### 3. Build Container Images
```bash
# Build backend image
cd backend
docker build -t todo-backend:latest .

# Build frontend image
cd ../frontend
docker build -t todo-frontend:latest .

# Verify images are built
docker images | grep todo
```

### 4. Prepare Helm Chart
```bash
# Navigate to Helm chart directory
cd ../k8s/helm/todo-app

# Install the Helm chart
helm install todo-app . --wait
```

### 5. Verify Installation
```bash
# Check all pods are running
kubectl get pods

# Check all services are available
kubectl get services

# Get frontend service URL
minikube service todo-frontend --url
```

### 6. Access the Application
```bash
# Open the frontend in your browser
minikube service todo-frontend

# Or get the URL to open manually
minikube service todo-frontend --url
```

## Troubleshooting

### Common Issues

#### Pods not starting
```bash
# Check pod status
kubectl get pods

# Check pod logs
kubectl logs <pod-name>

# Describe pod for detailed information
kubectl describe pod <pod-name>

# Use kubectl-ai for intelligent troubleshooting
kubectl-ai explain pod <pod-name>
```

#### Service not accessible
```bash
# Check service status
kubectl get services

# Check if service has an external IP
kubectl describe service todo-frontend

# Try port forwarding for debugging
kubectl port-forward svc/todo-frontend 8080:80
```

#### Database connection issues
```bash
# Check if database pod is running
kubectl get pods -l app=postgres

# Check database logs
kubectl logs <postgres-pod-name>

# Verify database connectivity from backend
kubectl exec -it <backend-pod-name> -- ping <postgres-service-name>
```

## Verification Steps

### 1. Check All Components
```bash
# Verify all pods are running (should show 1/1 Ready)
kubectl get pods

# Verify all services are available
kubectl get services

# Verify persistent volumes if using stateful database
kubectl get pv,pvc
```

### 2. Test Application Functionality
- Access the frontend via the Minikube service URL
- Create a new todo item
- Verify the item appears in the list
- Update the item status
- Delete the item

### 3. Verify Backend Connectivity
- Access the backend API directly if needed
- Test API endpoints manually or via API client
- Verify database operations are working

### 4. Use kagent for Health Check
```bash
# Run cluster health analysis
kagent analyze

# Check resource utilization
kagent resources
```

## Cleanup

### Uninstall the Application
```bash
# Uninstall the Helm release
helm uninstall todo-app

# Optionally stop Minikube
minikube stop

# Or delete the Minikube cluster completely
minikube delete
```

## Advanced Configuration

### Custom Values
Create a custom values file to override default configurations:
```bash
# Create custom values file
cp values.yaml my-values.yaml

# Edit my-values.yaml with custom configurations
# Install with custom values
helm install todo-app . -f my-values.yaml --wait
```

### Scaling
```bash
# Scale backend deployment
kubectl scale deployment todo-backend --replicas=3

# Check horizontal pod autoscaler if configured
kubectl get hpa
```

## Development Workflow

### Making Changes
1. Update code in backend or frontend directories
2. Rebuild the affected Docker image
3. Update the Helm chart if needed
4. Upgrade the Helm release: `helm upgrade todo-app . --wait`

### Local Development
- Use `kubectl port-forward` to access services locally
- Mount local code directories for live reloading
- Use development-specific Helm values