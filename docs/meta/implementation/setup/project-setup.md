# Project Setup Guide

## Overview

This guide covers the complete setup process for The Path (AI-Pi) development environment.

## Directory Structure

```
thepath-ai_pi/
├── server/                 # Go server
│   ├── cmd/               # Entry points
│   ├── internal/          # Internal packages
│   ├── pkg/               # Public packages
│   └── go.mod            # Go dependencies
├── client/                # TypeScript client
│   ├── src/              # Source code
│   ├── public/           # Static assets
│   └── package.json      # Node dependencies
├── ai/                    # Python AI system
│   ├── models/           # AI models
│   ├── training/         # Training system
│   └── requirements.txt  # Python dependencies
├── docs/                 # Documentation
├── scripts/              # Build/deploy scripts
└── docker/               # Docker configs
```

## Prerequisites

### Hardware Requirements
- Raspberry Pi 5 (8GB RAM recommended)
- AI HAT+ module
- Active cooling solution
- MicroSD card (32GB+ recommended)
- Optional: 7-inch touchscreen

### Software Requirements
- Go 1.21+
- Node.js 20+
- Python 3.11+
- Docker & Docker Compose
- Git

## Development Environment Setup

### 1. System Setup

```bash
# Update system
sudo apt update && sudo apt upgrade -y

# Install system dependencies
sudo apt install -y \
    build-essential \
    python3-dev \
    python3-pip \
    nodejs \
    npm \
    docker.io \
    docker-compose

# Enable Docker
sudo systemctl enable docker
sudo systemctl start docker
sudo usermod -aG docker $USER
```

### 2. Go Setup

```bash
# Install Go
wget https://go.dev/dl/go1.21.5.linux-arm64.tar.gz
sudo tar -C /usr/local -xzf go1.21.5.linux-arm64.tar.gz

# Add to PATH
echo 'export PATH=$PATH:/usr/local/go/bin' >> ~/.bashrc
source ~/.bashrc

# Verify installation
go version
```

### 3. Node.js Setup

```bash
# Install Node.js LTS
curl -fsSL https://deb.nodesource.com/setup_20.x | sudo -E bash -
sudo apt install -y nodejs

# Install development tools
npm install -g typescript ts-node nodemon

# Verify installation
node --version
npm --version
```

### 4. Python Setup

```bash
# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r ai/requirements.txt

# Verify installation
python --version
pip list
```

### 5. AI HAT+ Setup

```bash
# Install AI HAT+ drivers
curl -sSL https://raw.githubusercontent.com/arducam/arducam-config-parser-dev/master/install.sh | sudo bash

# Configure I2C
sudo raspi-config nonint do_i2c 0

# Test HAT+ connection
i2cdetect -y 1
```

## Project Setup

### 1. Clone Repository

```bash
# Clone project
git clone https://github.com/MaterDev/thepath-ai_pi.git
cd thepath-ai_pi

# Initialize git hooks
./scripts/init-hooks.sh
```

### 2. Server Setup

```bash
# Build server
cd server
go mod download
go build ./cmd/server

# Run tests
go test ./...
```

### 3. Client Setup

```bash
# Install dependencies
cd client
npm install

# Build client
npm run build

# Run tests
npm test
```

### 4. AI System Setup

```bash
# Setup AI environment
cd ai
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Run tests
python -m pytest
```

### 5. Development Database

```bash
# Start MongoDB
docker-compose -f docker/docker-compose.dev.yml up -d

# Verify connection
mongo mongodb://localhost:27017
```

## Running the Project

### Development Mode

```bash
# Terminal 1: Run server
cd server
go run ./cmd/server

# Terminal 2: Run client
cd client
npm run dev

# Terminal 3: Run AI system
cd ai
source venv/bin/activate
python -m ai.main
```

### Production Mode

```bash
# Build and run with Docker
docker-compose up --build
```

## Common Issues

### 1. Hardware Access

If you encounter permission issues with AI HAT+:
```bash
# Add user to required groups
sudo usermod -aG gpio,i2c $USER

# Reload groups
newgrp gpio
newgrp i2c
```

### 2. Memory Management

If you encounter memory issues:
```bash
# Adjust swap size
sudo dphys-swapfile swapoff
sudo nano /etc/dphys-swapfile
# Set CONF_SWAPSIZE=2048
sudo dphys-swapfile setup
sudo dphys-swapfile swapon
```

### 3. Performance Optimization

For optimal performance:
```bash
# Enable performance governor
echo "performance" | sudo tee /sys/devices/system/cpu/cpu*/cpufreq/scaling_governor

# Monitor temperature
vcgencmd measure_temp
```

## Development Tools

### 1. VSCode Setup

Recommended extensions:
- Go
- Python
- TypeScript
- Docker
- Remote - SSH

### 2. Git Configuration

```bash
# Configure Git
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"

# Setup pre-commit hooks
pre-commit install
```

### 3. Testing Tools

```bash
# Install testing tools
go install github.com/golang/mock/mockgen@v1.6.0
npm install -g jest
pip install pytest pytest-cov
```

## Version History
- v1.0: Initial setup guide
- v1.1: Added Docker setup
- v1.2: Updated dependencies
