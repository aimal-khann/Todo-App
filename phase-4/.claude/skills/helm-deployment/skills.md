name: Helm Deployment Blueprint
description: A dynamic Kubernetes Deployment manifest using Go templating for Helm.
model: sonnet
---
Reusable Skill:
Skill: Helm Deployment Blueprint – Input: appName: string, hasDatabase: boolean; Output: A deployment.yaml template string with Go templating logic.

Architectural Details:
- **Metadata:** Dynamic labels using `{{ include "todo-app.selectorLabels" . }}` helper.
- **Replicas:** Configurable via `{{ .Values.replicaCount }}`.
- **Update Strategy:** `RollingUpdate` to ensure zero downtime.
- **Config Injection:** - Environment variables loaded from `ConfigMap` (`envFrom: - configMapRef`).
  - Secrets loaded safely (`envFrom: - secretRef`).
- **Observability:** Liveness and Readiness probes configured by default pointing to `{{ .Values.service.port }}`.

Usage Example:
apiVersion: apps/v1
kind: Deployment
metadata:
  name: {{ include "todo-app.fullname" . }}-backend
  labels:
    {{- include "todo-app.labels" . | nindent 4 }}
spec:
  replicas: {{ .Values.backend.replicaCount }}
  selector:
    matchLabels:
      {{- include "todo-app.selectorLabels" . | nindent 6 }}
      app.kubernetes.io/component: backend
  template:
    metadata:
      labels:
        {{- include "todo-app.selectorLabels" . | nindent 8 }}
        app.kubernetes.io/component: backend
    spec:
      containers:
        - name: backend
          image: "{{ .Values.backend.image.repository }}:{{ .Values.backend.image.tag }}"
          ports:
            - containerPort: 8000
          envFrom:
            - secretRef:
                name: {{ include "todo-app.fullname" . }}-secrets