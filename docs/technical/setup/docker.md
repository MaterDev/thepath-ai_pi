# Docker Setup

## Overview

The project uses Docker for local development and deployment. Each service runs in its own container with health monitoring.

## Development Environment

### 1. Prerequisites

- Docker Engine 20.10+
- Docker Compose 2.2+
- Make (optional, for convenience scripts)

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

```dockerfile
# dev/client.Dockerfile
FROM node:18-alpine
WORKDIR /app/client
COPY package*.json ./
RUN npm install
COPY . .
EXPOSE 3000
CMD ["npm", "start"]

# dev/server.Dockerfile
FROM golang:1.21-alpine
WORKDIR /app/server
COPY go.* ./
RUN go mod download
COPY . .
EXPOSE 8080
CMD ["go", "run", "cmd/main.go"]

# dev/ai.Dockerfile
FROM python:3.11-slim
WORKDIR /app/ai
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["python", "main.py"]
```

### 5. Docker Compose

```yaml
version: '3.8'

services:
  client:
    build:
      context: ./client
      dockerfile: ../docker/dev/client.Dockerfile
    volumes:
      - ./client:/app/client
      - /app/client/node_modules
    ports:
      - "3000:3000"
    environment:
      - NODE_ENV=development
      - REACT_APP_API_URL=http://localhost:8080
    healthcheck:
      test: ["CMD", "wget", "-qO-", "http://localhost:3000/health"]
      interval: 30s
      timeout: 10s
      retries: 3

  server:
    build:
      context: ./server
      dockerfile: ../docker/dev/server.Dockerfile
    volumes:
      - ./server:/app/server
    ports:
      - "8080:8080"
    environment:
      - GO_ENV=development
      - MONGO_URI=mongodb://mongodb:27017
      - AI_SERVICE_URL=http://ai:5000
    depends_on:
      - mongodb
    healthcheck:
      test: ["CMD", "wget", "-qO-", "http://localhost:8080/health"]
      interval: 30s
      timeout: 10s
      retries: 3

  ai:
    build:
      context: ./ai
      dockerfile: ../docker/dev/ai.Dockerfile
    volumes:
      - ./ai:/app/ai
    ports:
      - "5000:5000"
    environment:
      - PYTHON_ENV=development
      - MODEL_PATH=/app/ai/models
    healthcheck:
      test: ["CMD", "wget", "-qO-", "http://localhost:5000/health"]
      interval: 30s
      timeout: 10s
      retries: 3

  mongodb:
    image: mongo:5
    ports:
      - "27017:27017"
    volumes:
      - mongodb_data:/data/db
    healthcheck:
      test: ["CMD", "mongosh", "--eval", "db.adminCommand('ping')"]
      interval: 30s
      timeout: 10s
      retries: 3

volumes:
  mongodb_data:
```

## Health Monitoring

### 1. Health Check Endpoints

Each service implements a `/health` endpoint that returns:
- Service status
- Timestamp
- Version information
- Dependencies status

Example response:
```json
{
  "status": "healthy",
  "timestamp": 1642561234567,
  "version": "1.0.0",
  "service": "server",
  "dependencies": {
    "mongodb": "connected",
    "ai_service": "connected"
  }
}
```

### 2. Health Check Implementation

```typescript
// Client health check (React)
app.get('/health', (req, res) => {
    res.json({
        status: 'healthy',
        timestamp: Date.now(),
        version: process.env.npm_package_version,
        service: 'client',
        dependencies: {
            api: checkApiConnection()
        }
    });
});
```

```go
// Server health check (Go)
func healthHandler(w http.ResponseWriter, r *http.Request) {
    health := struct {
        Status       string            `json:"status"`
        Timestamp    int64            `json:"timestamp"`
        Version      string           `json:"version"`
        Service      string           `json:"service"`
        Dependencies map[string]string `json:"dependencies"`
    }{
        Status:    "healthy",
        Timestamp: time.Now().UnixMilli(),
        Version:   "1.0.0",
        Service:   "server",
        Dependencies: map[string]string{
            "mongodb":     checkMongoConnection(),
            "ai_service": checkAiConnection(),
        },
    }
    json.NewEncoder(w).Encode(health)
}
```

```python
# AI service health check (Python)
@app.route('/health')
def health():
    return jsonify({
        'status': 'healthy',
        'timestamp': int(time.time() * 1000),
        'version': '1.0.0',
        'service': 'ai',
        'dependencies': {
            'model': check_model_loaded()
        }
    })
```

## Development Workflow

### 1. Starting Services

```bash
# Build and start all services
docker-compose up -d

# View logs
docker-compose logs -f

# Check service status
docker-compose ps
```

### 2. Health Monitoring

```bash
# Check all service health
./scripts/check-health.sh

# View specific service health
curl http://localhost:3000/health  # Client
curl http://localhost:8080/health  # Server
curl http://localhost:5000/health  # AI
```

### 3. Stopping Services

```bash
# Stop all services
docker-compose down

# Stop and remove volumes
docker-compose down -v
```

## Production Deployment

### 1. Building Production Images

```bash
# Build production images
docker-compose -f docker-compose.prod.yml build

# Push images to registry
docker-compose -f docker-compose.prod.yml push
```

### 2. Release Process

```bash
# Create release
./scripts/release.sh 1.0.0

# Tag images
docker tag aipi-client:latest aipi-client:1.0.0
docker tag aipi-server:latest aipi-server:1.0.0
docker tag aipi-ai:latest aipi-ai:1.0.0
```

## Version History
- v1.0: Initial Docker setup
- v1.1: Added health monitoring
- v1.2: Enhanced production deployment
- v2.0: Updated for simplified battle mechanics
