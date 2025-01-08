# Project Dependencies

## Overview

This document lists all project dependencies and their versions to ensure consistent development and deployment.

## Server Dependencies (Go)

```go
// go.mod
module github.com/MaterDev/thepath-ai_pi

go 1.21

require (
    github.com/gorilla/websocket v1.5.1
    github.com/gin-gonic/gin v1.9.1
    go.mongodb.org/mongo-driver v1.13.1
    github.com/stretchr/testify v1.8.4
    github.com/spf13/viper v1.18.2
    github.com/prometheus/client_golang v1.17.0
    github.com/sirupsen/logrus v1.9.3
    golang.org/x/sync v0.5.0
)
```

## Client Dependencies (TypeScript)

```json
{
  "dependencies": {
    "react": "^18.2.0",
    "react-dom": "^18.2.0",
    "redux": "^5.0.0",
    "react-redux": "^9.0.4",
    "@reduxjs/toolkit": "^2.0.1",
    "typescript": "^5.3.3",
    "axios": "^1.6.2",
    "socket.io-client": "^4.7.2",
    "tailwindcss": "^3.3.6",
    "three.js": "^0.159.0"
  },
  "devDependencies": {
    "@types/react": "^18.2.45",
    "@types/react-dom": "^18.2.18",
    "@typescript-eslint/eslint-plugin": "^6.15.0",
    "@typescript-eslint/parser": "^6.15.0",
    "eslint": "^8.56.0",
    "jest": "^29.7.0",
    "@testing-library/react": "^14.1.2",
    "vite": "^5.0.10"
  }
}
```

## AI System Dependencies (Python)

```python
# requirements.txt

# Core Dependencies
numpy==1.26.2
torch==2.1.1
transformers==4.35.2
scikit-learn==1.3.2
pandas==2.1.3

# Hardware Acceleration
tflite-runtime==2.14.0
onnxruntime==1.16.3
tensorrt==8.6.1

# Data Management
pymongo==4.6.1
redis==5.0.1
pyyaml==6.0.1

# Monitoring & Logging
prometheus-client==0.19.0
tensorboard==2.15.1
wandb==0.16.1

# Testing
pytest==7.4.3
pytest-cov==4.1.0
pytest-asyncio==0.21.1

# Development
black==23.11.0
isort==5.12.0
mypy==1.7.1
pylint==3.0.2
```

## System Requirements

### Hardware
- Raspberry Pi 5 (8GB RAM recommended)
- AI HAT+ module
- Active cooling solution
- 32GB+ MicroSD card
- Optional: 7-inch touchscreen

### Operating System
- Raspberry Pi OS (64-bit)
- Kernel version: 6.1+
- Python 3.11+
- Node.js 20+
- Go 1.21+

### Development Tools
- Docker 24+
- Docker Compose 2.23+
- Git 2.42+
- VSCode 1.84+

## Database

```yaml
# MongoDB
version: '6.0'
replica_set: true
wiredTiger:
  engineConfig:
    cacheSizeGB: 0.5
```

## Infrastructure

```yaml
# docker-compose.yml
version: '3.8'

services:
  server:
    build: ./server
    image: thepath-ai_pi/server:latest
    depends_on:
      - mongodb
      - redis

  client:
    build: ./client
    image: thepath-ai_pi/client:latest
    depends_on:
      - server

  ai:
    build: ./ai
    image: thepath-ai_pi/ai:latest
    devices:
      - "/dev/i2c-1:/dev/i2c-1"
    depends_on:
      - server

  mongodb:
    image: mongo:6.0
    volumes:
      - mongodb_data:/data/db

  redis:
    image: redis:7.2
    volumes:
      - redis_data:/data
```

## Development Tools

### VSCode Extensions
- Go
- Python
- TypeScript and JavaScript
- ESLint
- Prettier
- Docker
- Remote - SSH
- GitLens

### Git Hooks
```bash
# pre-commit
#!/bin/sh
go fmt ./...
go vet ./...
npm run lint
black ai/
isort ai/
pylint ai/
```

## Version Control

```yaml
# .gitignore
node_modules/
dist/
venv/
__pycache__/
*.pyc
.env
.env.*
*.log
coverage/
.DS_Store
```

## Related Documentation
- [Project Setup](../implementation/setup/project-setup.md)
- [Contributing Guide](../meta/contributing.md)
- [Style Guide](../meta/style-guide.md)
