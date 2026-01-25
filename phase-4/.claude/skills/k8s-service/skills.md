name: K8s Service Definition
description: A reusable template for defining Kubernetes Services (ClusterIP vs NodePort).
model: sonnet
---
Reusable Skill:
Skill: K8s Service Definition – Input: type: 'ClusterIP' | 'NodePort' | 'LoadBalancer', port: number, targetPort: number; Output: A service.yaml template.

Architectural Details:
- **Type Handling:** Logic to toggle between `ClusterIP` (Backend/DB) and `NodePort` (Frontend) based on values.
- **Selector:** Strictly matches the Pod labels defined in the Deployment blueprint.
- **Port Mapping:** Clearly distinguishes between `port` (Service port) and `targetPort` (Container port).
- **Session Affinity:** Optional `ClientIP` configuration if sticky sessions are needed (rare for stateless apps).

Usage Example:
apiVersion: v1
kind: Service
metadata:
  name: {{ include "todo-app.fullname" . }}-frontend
  labels:
    {{- include "todo-app.labels" . | nindent 4 }}
spec:
  type: {{ .Values.frontend.service.type }}
  ports:
    - port: {{ .Values.frontend.service.port }}
      targetPort: 3000
      protocol: TCP
      name: http
  selector:
    {{- include "todo-app.selectorLabels" . | nindent 4 }}
    app.kubernetes.io/component: frontend