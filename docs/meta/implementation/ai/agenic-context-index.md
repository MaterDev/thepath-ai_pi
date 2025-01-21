# AI Development Index

## Purpose

This document serves as a master reference for AI agents during development of The Path (AI-Pi). It indexes essential resources and documentation across the project.

## Quick Links

### Essential Documentation
- [Project Scope](../../../overview/project-scope.md)
- [Research Objectives](../../../overview/research-objectives.md)
- [System Architecture](../../../overview/system-architecture.md)
- [Development Logs](../../logs/index.md)

### Core Systems
- [AI Architecture](architecture.md)
- [Client Architecture](../client/architecture.md)
- [Server Architecture](../server/architecture.md)

## Project Resources

### Repository Structure
```yaml
Root_Directories:
  docs: "Documentation and specifications"
  src: "Source code"
  tests: "Test files"
  scripts: "Build and utility scripts"
  images: "Project images and assets"

Documentation_Structure:
  overview: "High-level project documentation"
  technical: "Technical specifications and APIs"
  implementation: "Implementation details and planning"
  meta: "Project metadata and phase documentation"
  health: "Service health monitoring"
```

## System Architecture

### AI Pipeline
```yaml
Training_Environment:
  platform: "Mac Mini M1"
  components:
    - training_pipeline: "technical/ai-system/training-pipeline.md"
    - ai_models: "technical/data-schemas/ai-models.md"
    - behavior_model: "technical/ai-system/behavior-model.md"

Inference_Environment:
  platform: "Raspberry Pi 5"
  components:
    - hardware: "technical/hardware/raspberry-pi-5.md"
    - ai_hat: "technical/hardware/ai-hat-plus.md"
    - difficulty: "technical/ai-system/difficulty-system.md"
```

### Game Systems
```yaml
State_Management:
  components:
    - game_state: "technical/data-schemas/game-state.md"
    - replay_system: "technical/data-schemas/replay-system.md"

Battle_System:
  components:
    - turn_system: "meta/phase1/5-turn-system.md"
    - communication: "meta/phase1/3-communication.md"
```

### Infrastructure
```yaml
Development_Environment:
  components:
    - docker: "technical/setup/docker.md"
    - setup: "meta/phase1/1-project-setup.md"

Health_Monitoring:
  components:
    - overview: "technical/health/index.md"
    - ai_service: "technical/health/ai.md"
    - client: "technical/health/client.md"
    - server: "technical/health/server.md"
```

## Implementation Guide

### Phase 1: Core Systems
```yaml
Setup:
  document: "meta/phase1/1-project-setup.md"
  components:
    - docker_containers: "Container configuration"
    - service_setup: "Service initialization"
    - health_monitoring: "Health check system"

Game_State:
  document: "meta/phase1/2-game-state.md"
  components:
    - state_management: "State handling"
    - data_schemas: "Data structures"
    - persistence: "Data storage"

Communication:
  document: "meta/phase1/3-communication.md"
  components:
    - websocket: "WebSocket protocol"
    - events: "Event handling"
    - recovery: "Error recovery"

AI_Integration:
  document: "meta/phase1/4-ai-integration.md"
  components:
    - model_deployment: "Model setup"
    - inference: "Inference pipeline"
    - optimization: "Performance tuning"

Turn_System:
  document: "meta/phase1/5-turn-system.md"
  components:
    - mechanics: "Battle mechanics"
    - actions: "Action handling"
    - transitions: "State transitions"
```

### Technology Stack
```yaml
Client:
  framework: "React + TypeScript"
  ui: "Material-UI"
  state: "Redux"
  protocol: "WebSocket"

Server:
  language: "Go"
  database: "MongoDB"
  protocol: "WebSocket"
  container: "Docker"

AI_Service:
  runtime: "Python"
  model: "TensorFlow Lite"
  training: "Mac Mini M1"
  inference: "Raspberry Pi 5"
```

### Character System
```yaml
Classes:
  conjuror:
    document: "combat_system/classes/conjuror.md"
  crystal_vanguard:
    document: "combat_system/classes/crystal_vanguard.md"
  primal_shifter:
    document: "combat_system/classes/primal_shifter.md"
  the_blessed:
    document: "combat_system/classes/the_blessed.md"
  zealot:
    document: "combat_system/classes/zealot.md"
```

## Development Resources

### Documentation Tree
```yaml
Structure:
  overview: "Project overview and objectives"
  technical:
    ai-system: "AI system implementation"
    data-schemas: "Data structures and models"
    hardware: "Hardware specifications"
    health: "Health monitoring"
    setup: "Development setup"
  meta:
    phase1: "Phase 1 implementation"
```

### Analysis
```yaml
Documents:
  analysis: "meta/analysis/documentation-analysis.md"
  research: "overview/research-objectives.md"
  architecture: "overview/system-architecture.md"
```

### Development Logs
```yaml
Latest_Updates:
  - "meta/logs/2025-01-17.md"
  - "meta/logs/2025-01-15.md"
  - "meta/logs/2025-01-13.md"
```

### Monitoring
* AI performance
* Decision quality
* Resource usage
* Error tracking
