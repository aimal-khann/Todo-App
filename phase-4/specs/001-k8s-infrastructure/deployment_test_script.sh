#!/bin/bash

# Deployment and Testing Script for Todo App on Minikube

set -e  # Exit on any error

echo "🚀 Starting Todo App deployment to Minikube..."

# Check if minikube is running
if ! minikube status &> /dev/null; then
    echo "🔴 Minikube is not running. Starting minikube..."
    minikube start --cpus=4 --memory=8192 --disk-size=20g
else
    echo "✅ Minikube is already running"
fi

# Set Docker environment to use Minikube's Docker daemon
echo "🐳 Setting Docker environment to Minikube..."
eval $(minikube -p minikube docker-env)

# Build Docker images
echo "🏗️ Building Docker images..."
cd backend
docker build -t todo-backend:v1 .
cd ../frontend
docker build -t todo-frontend:v1 .
cd ..

echo "✅ Docker images built successfully"

# Verify images exist
echo "🔍 Verifying Docker images..."
docker images | grep todo-

# Install the Helm chart
echo "🚢 Installing Helm chart..."
helm uninstall todo-app 2>/dev/null || true  # Remove if exists
helm install todo-app ./k8s/helm/todo-app --wait

echo "✅ Helm chart installed successfully"

# Wait a moment for pods to start
sleep 10

# Check all pods are running
echo "_Pods status:"
kubectl get pods

# Check all services are available
echo "🌐 Services status:"
kubectl get services

# Wait for all pods to be ready
echo "⏳ Waiting for all pods to be ready..."
kubectl wait --for=condition=ready pod -l app=backend --timeout=300s
kubectl wait --for=condition=ready pod -l app=frontend --timeout=300s
kubectl wait --for=condition=ready pod -l app=postgresql --timeout=300s

echo "✅ All pods are running and ready!"

# Get the frontend service URL
FRONTEND_URL=$(minikube service todo-frontend --url)
echo "🌍 Frontend URL: $FRONTEND_URL"

# Test the backend service connectivity
BACKEND_URL=$(minikube service todo-backend --url)
echo "📡 Backend URL: $BACKEND_URL"

# Test basic connectivity
echo "🔗 Testing connectivity..."
if curl -f $BACKEND_URL/health &> /dev/null; then
    echo "✅ Backend health check passed"
else
    echo "❌ Backend health check failed"
fi

# Test frontend is accessible
if curl -f $FRONTEND_URL &> /dev/null; then
    echo "✅ Frontend is accessible"
else
    echo "⚠️ Frontend may not be accessible yet, waiting..."
    sleep 30
    if curl -f $FRONTEND_URL &> /dev/null; then
        echo "✅ Frontend is now accessible"
    else
        echo "❌ Frontend is not accessible"
    fi
fi

echo "🎉 Deployment and basic testing completed!"
echo ""
echo "To access the application:"
echo "Frontend: $FRONTEND_URL"
echo "Backend: $BACKEND_URL"
echo ""
echo "To check logs:"
echo "kubectl logs -l app=backend"
echo "kubectl logs -l app=frontend"
echo "kubectl logs -l app=postgresql"