# Debugging Workflow with kubectl-ai and kagent

## Overview
This document outlines the debugging workflow using kubectl-ai and kagent for the Todo App deployed on Kubernetes.

## Pod Connectivity Issues

### Scenario: Frontend Cannot Reach Backend

When experiencing connectivity issues between frontend and backend pods, use kubectl-ai to diagnose:

```bash
# Check if frontend can reach backend
kubectl-ai explain "check why frontend cannot reach backend"

# Get detailed pod connectivity information
kubectl-ai logs todo-frontend-<pod-id> --context
kubectl-ai logs todo-backend-<pod-id> --context

# Check service endpoints
kubectl-ai explain endpoints todo-backend
```

### Common Connectivity Issues and Solutions

1. **DNS Resolution Issues**:
   ```bash
   kubectl-ai explain "pod cannot resolve service name"
   ```

2. **Network Policy Blocking**:
   ```bash
   kubectl-ai explain "check network policies for todo-backend"
   ```

3. **Service Port Misconfiguration**:
   ```bash
   kubectl-ai explain service todo-backend
   ```

## Troubleshooting Pod Crashes

### Using kubectl-ai for Crash Diagnosis

When a pod is in CrashLoopBackOff state:

```bash
# Explain the crash reason
kubectl-ai explain pod todo-backend-<pod-id>

# Check container logs with AI context
kubectl-ai logs todo-backend-<pod-id> --context

# Get resource usage analysis
kubectl-ai describe pod todo-backend-<pod-id>
```

## Resource Analysis with kagent

### Analyze Cluster Health

```bash
# Overall cluster health analysis
kagent analyze

# Resource usage overview
kagent resources

# Identify resource bottlenecks
kagent analyze --focus resources
```

### Performance Optimization

```bash
# Check for resource optimization opportunities
kagent optimize

# Analyze pod resource requests vs usage
kagent analyze --focus efficiency
```

## Validation Workflow

### Pre-deployment Validation

```bash
# Validate configuration before deployment
kagent validate ./k8s/helm/todo-app

# Check security posture
kagent analyze --focus security
```

### Post-deployment Validation

```bash
# Verify deployment health
kagent analyze --focus health

# Check resource optimization
kagent resources --focus optimization
```

## Common Debugging Commands

### Basic Diagnostics
```bash
# Pod status with AI insights
kubectl-ai get pods

# Service connectivity check
kubectl-ai get svc

# Describe with AI interpretation
kubectl-ai describe deployment todo-frontend
```

### Advanced Diagnostics
```bash
# Network connectivity analysis
kubectl-ai explain "network connectivity between pods"

# Resource constraint analysis
kubectl-ai explain "resource constraints for deployment"

# Configuration validation
kubectl-ai explain "configuration issues for todo-app"
```

## Troubleshooting Checklist

1. **Verify Pod Status**:
   - Are all pods running?
   - Are there any restarts?
   - Are readiness/liveness probes passing?

2. **Check Service Discovery**:
   - Can pods resolve service names?
   - Are services correctly exposing ports?
   - Are endpoints populated?

3. **Validate Network Policies**:
   - Are there any blocking network policies?
   - Is traffic flowing as expected?

4. **Review Resource Constraints**:
   - Are there CPU/memory limits causing issues?
   - Are requests/reservations appropriate?

5. **Examine Logs**:
   - Are there application-level errors?
   - Any infrastructure-related issues?

## Integration with CI/CD

### Automated Validation
```bash
# Run automated validation in CI
kagent validate --exit-on-error

# Generate health reports
kagent analyze --format json > health-report.json
```

This workflow ensures efficient troubleshooting of the Todo App deployment on Kubernetes using AI-assisted tools.