# Data Model: Local Kubernetes Infrastructure (Phase IV)

## Overview
This document defines the data entities and their relationships for the Kubernetes infrastructure implementation of the Todo App.

## Core Entities

### Todo Task
**Description**: Represents individual todo items with properties like title, description, status, and timestamps

**Fields**:
- id: UUID (primary key)
- title: String (required, max 255 chars)
- description: Text (optional)
- status: Enum (pending, in-progress, completed)
- created_at: DateTime (timestamp)
- updated_at: DateTime (timestamp)
- user_id: UUID (foreign key to User)

**Relationships**:
- Belongs to one User
- Has many Attachments (optional)

### User Session
**Description**: Represents authenticated user sessions with associated data and preferences

**Fields**:
- session_id: String (primary key)
- user_id: UUID (foreign key to User)
- created_at: DateTime (timestamp)
- expires_at: DateTime (timestamp)
- ip_address: String (optional)
- user_agent: String (optional)

**Relationships**:
- Belongs to one User

### Database Connection
**Description**: Represents the connection between backend and database for storing todo items

**Fields**:
- connection_id: String (primary key)
- host: String (database host)
- port: Integer (database port)
- database_name: String (database name)
- username: String (database user)
- ssl_enabled: Boolean (whether SSL is enabled)

## Kubernetes Configuration Entities

### Deployment Configuration
**Description**: Configuration for Kubernetes deployments

**Fields**:
- name: String (deployment name)
- replicas: Integer (number of replicas)
- image: String (container image)
- image_pull_policy: String (Always, IfNotPresent, Never)
- resources_requests_cpu: String (CPU request)
- resources_requests_memory: String (memory request)
- resources_limits_cpu: String (CPU limit)
- resources_limits_memory: String (memory limit)

### Service Configuration
**Description**: Configuration for Kubernetes services

**Fields**:
- name: String (service name)
- type: String (ClusterIP, NodePort, LoadBalancer)
- port: Integer (service port)
- target_port: Integer (target port)
- protocol: String (TCP, UDP)

### Secret Configuration
**Description**: Configuration for Kubernetes secrets

**Fields**:
- name: String (secret name)
- type: String (Opaque, kubernetes.io/tls, etc.)
- data: Map (key-value pairs of sensitive data)

### ConfigMap Configuration
**Description**: Configuration for Kubernetes ConfigMaps

**Fields**:
- name: String (configmap name)
- data: Map (key-value pairs of non-sensitive data)

## State Transitions

### Todo Task Status Transitions
- pending → in-progress
- in-progress → completed
- completed → pending (reopening)
- in-progress → pending (cancellation)

### User Session States
- active → expired
- active → terminated (logout)
- inactive → active (login)