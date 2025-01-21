# Project Dependencies

## Overview

This document lists all project dependencies and their versions to ensure consistent development and deployment.

## Server Dependencies (Go)

```go
// go.mod
module github.com/mater-dev/thepath-ai_pi

go 1.21

require (
    github.com/gorilla/websocket v1.5.1
    github.com/gin-gonic/gin v1.9.1
    github.com/golang-jwt/jwt/v5 v5.2.0
    github.com/google/uuid v1.5.0
    go.mongodb.org/mongo-driver v1.13.1
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
    "@mui/material": "^5.15.0",
    "@mui/icons-material": "^5.15.0",
    "@emotion/react": "^11.11.1",
    "@emotion/styled": "^11.11.0",
    "typescript": "^5.3.3",
    "axios": "^1.6.2",
    "socket.io-client": "^4.7.2"
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

## AI Dependencies (Python)

```python
# requirements.txt
tensorflow-lite==2.14.0
numpy==1.24.3
pandas==2.1.4
scikit-learn==1.3.2
flask==3.0.0
gunicorn==21.2.0
prometheus-client==0.19.0
```

## Development Tools

### Version Control
* Git 2.39+
* GitHub CLI 2.0+
* Git LFS 3.0+

### Build Tools
* Docker 20.10+
* Docker Compose 2.2+
* Make 4.3+

### Code Quality
* ESLint 8.56+
* Prettier 3.1+
* golangci-lint 1.55+
* black 23.12+
* isort 5.13+

### Testing
* Jest 29.7+
* React Testing Library 14.1+
* Go testing
* pytest 7.4+

## Infrastructure Dependencies

### Databases
* MongoDB 5.0+
* Redis 7.0+ (optional)

### Monitoring
* Prometheus 2.45+
* Grafana 10.2+

### CI/CD
* GitHub Actions
* Docker Registry
* Ansible 2.15+

## Hardware Requirements

### Development
* CPU: 4+ cores
* RAM: 8GB+
* Storage: 20GB+
* OS: Linux/macOS/Windows

### Production (Raspberry Pi 5)
* CPU: BCM2712
* RAM: 8GB
* Storage: 32GB+
* AI HAT+: Coral Edge TPU

## Version Control

### Git Configuration
* LFS for model files
* Husky for pre-commit hooks
* Conventional commits

### Branching Strategy
* main: production
* develop: integration
* feature/*: features
* bugfix/*: bug fixes

## Dependency Management

### Update Policy
* Security updates: Immediate
* Major versions: Quarterly
* Minor versions: Monthly
* Patches: Weekly

### Version Constraints
* Production: Fixed versions
* Development: Caret ranges
* CI/CD: Latest stable

## Container Images

### Base Images
* Go: golang:1.21-alpine
* Node: node:18-alpine
* Python: python:3.11-slim
* MongoDB: mongo:5

### Custom Images
* Server: thepath-ai_pi/server
* Client: thepath-ai_pi/client
* AI: thepath-ai_pi/ai
