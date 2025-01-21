# Docker Setup

## Overview

The project uses Docker for local development and deployment. Each service runs in its own container with health monitoring.

## Development Environment

### 1. Prerequisites

* Docker Engine 20.10+
* Docker Compose 2.2+
* Make (optional, for convenience scripts)

### 2. Directory Structure

```
aipi/
├── docker/
│   ├── dev/
│   │   ├── client.Dockerfile
│   │   ├── server.Dockerfile
│   │   └── ai.Dockerfile
│   └── prod/
│       ├── client.Dockerfile
│       ├── server.Dockerfile
│       └── ai.Dockerfile
└── docker-compose.yml
```

### 3. Base Images

```dockerfile
# dev/base.Dockerfile
FROM ubuntu:22.04

# Install common dependencies
RUN apt-get update && apt-get install -y \
    curl \
    wget \
    git \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Set environment
ENV DEBIAN_FRONTEND=noninteractive
ENV TZ=UTC
```

### 4. Service Images

#### Client Service
* React development server
* Hot reloading enabled
* Development tools mounted
* Port 3000 exposed

#### Server Service
* Go development environment
* Live reload with Air
* Debug port exposed
* Health monitoring

#### AI Service
* Python development environment
* TensorFlow Lite runtime
* Model files mounted
* Health monitoring

## Configuration

### Environment Variables

#### Development
* `DOCKER_BUILDKIT=1`: Enable BuildKit
* `COMPOSE_DOCKER_CLI_BUILD=1`: Use BuildKit
* `NODE_ENV=development`: Client mode
* `GO_ENV=development`: Server mode
* `PYTHON_ENV=development`: AI mode

#### Production
* `NODE_ENV=production`: Client mode
* `GO_ENV=production`: Server mode
* `PYTHON_ENV=production`: AI mode
* `TZ=UTC`: Timezone setting

### Volume Mounts

#### Development
* Source code directories
* Node modules
* Go modules
* Python virtual environment
* Development tools

#### Production
* Configuration files
* SSL certificates
* Static assets
* Model files

## Health Monitoring

### Endpoints

#### Client Service
* Health check: `:3000/health`
* Metrics: `:3000/metrics`
* Status: `:3000/status`

#### Server Service
* Health check: `:8080/health`
* Metrics: `:8080/metrics`
* Status: `:8080/status`

#### AI Service
* Health check: `:5000/health`
* Metrics: `:5000/metrics`
* Status: `:5000/status`

### Monitoring Tools
* Container stats
* Resource usage
* Error logging
* Performance metrics

## Usage

### Development

#### 1. Starting Services
```bash
# Build and start all services
docker-compose up -d
```

#### 2. Viewing Logs
```bash
# All services
docker-compose logs -f

# Specific service
docker-compose logs -f [service]
```

#### 3. Stopping Services
```bash
# Stop all services
docker-compose down

# Stop and remove volumes
docker-compose down -v
```

### Production

#### 1. Building Images
```bash
# Build all services
docker-compose -f docker-compose.prod.yml build

# Build specific service
docker-compose -f docker-compose.prod.yml build [service]
```

#### 2. Deployment
```bash
# Start production stack
docker-compose -f docker-compose.prod.yml up -d

# Scale services
docker-compose -f docker-compose.prod.yml up -d --scale [service]=N
```

## Troubleshooting

### Common Issues
* Container startup failures
* Network connectivity
* Volume permissions
* Resource constraints

### Debug Tools
* Container logs
* Health check endpoints
* Resource monitoring
* Network inspection
