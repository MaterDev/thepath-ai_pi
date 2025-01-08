# The Path (AI-Pi)

An edge AI-powered turn-based combat game running on Raspberry Pi hardware.

## Overview

The Path (AI-Pi) is a research project exploring edge AI capabilities through a turn-based combat system running on Raspberry Pi hardware. The project demonstrates sophisticated AI behavior running entirely on local hardware, providing unique insights into edge AI gaming.

## AI-First Development Approach

This project uses a unique "AI-First" development methodology, specifically designed for working with agentic IDE tools like Windsurf. The approach focuses on creating comprehensive documentation before development begins, serving as a contextual framework for AI tools.

### Documentation Structure

```
docs/
├── AI_DEVELOPMENT_INDEX.md    # Master reference for AI tools
├── overview/                  # High-level project documentation
│   ├── project-scope.md      # Detailed project specifications
│   ├── system-architecture.md # System design and components
│   └── research-objectives.md # Research goals and metrics
├── implementation/           # Implementation details
│   ├── server/              # Server implementation docs
│   ├── client/              # Client implementation docs
│   └── ai/                  # AI system docs
├── technical/               # Technical specifications
│   ├── api/                # API documentation
│   ├── data-schemas/       # Data structure definitions
│   └── hardware/           # Hardware configurations
└── meta/                   # Project metadata
    ├── style-guide.md      # Coding standards
    └── contributing.md     # Contribution guidelines
```

### AI-First Documentation Approach

#### 1. Purpose
The documentation structure is specifically designed to:
- Provide consistent context for AI tools
- Enable efficient development with limited context windows
- Maintain project coherence across multiple sessions
- Guide AI in making implementation decisions

#### 2. Key Components

##### AI Development Index
- Master reference document
- Always kept in context
- Contains critical specifications
- Guides documentation updates

##### Project Scope
- Detailed timeline
- Task dependencies
- Implementation priorities
- Success criteria

##### Technical Specifications
- API definitions
- Data schemas
- Performance requirements
- Hardware configurations

#### 3. How It Works

1. **Context Management**
   - AI tools maintain the AI Development Index in context
   - Index provides quick access to critical information
   - Reduces context switching and information loss

2. **Decision Guidance**
   - Clear specifications guide AI decisions
   - Consistent reference points
   - Defined success criteria
   - Implementation priorities

3. **Documentation Updates**
   - Structured update process
   - Cross-reference validation
   - Version control guidelines
   - Consistency checks

4. **Development Flow**
   - Review specifications
   - Reference detailed docs
   - Implement features
   - Update documentation

### Benefits of AI-First Approach

1. **Enhanced AI Capabilities**
   - Better context understanding
   - More consistent decisions
   - Reduced errors
   - Faster development

2. **Project Coherence**
   - Consistent implementation
   - Clear dependencies
   - Maintained standards
   - Tracked progress

3. **Efficient Development**
   - Reduced context switching
   - Clear priorities
   - Defined processes
   - Quick reference

4. **Quality Assurance**
   - Built-in validation
   - Performance tracking
   - Documentation alignment
   - Error prevention

## Core Features

### Edge AI Combat System
- Real-time AI decision making (<100ms)
- Adaptive difficulty (0.2-0.95)
- Personality-based behavior
- Hardware acceleration

### Turn-Based Combat
- Speed-based turn order
- Action point system
- Reaction mechanics
- Status effects

### Character System
- Multiple classes
- Stat-based progression
- Equipment system
- Skill trees

### Game Client
- Responsive UI (<16ms)
- Real-time updates
- Combat animations
- Touch support

## Technical Stack

### Server (Go 1.21+)
- Game state management
- WebSocket communication
- Performance optimization
- State serialization

### Client (TypeScript/React)
- User interface
- State management
- Network layer
- Animations

### AI System (Python 3.11+)
- Behavior models
- Training pipeline
- Difficulty system
- Hardware acceleration

### Hardware
- Raspberry Pi 5
- 8GB RAM
- AI HAT+ module
- Active cooling

## Development Timeline

See [Project Scope](docs/overview/project-scope.md) for the detailed timeline and tasks.

### Quick Overview
- **Phase 1 (Weeks 1-2)**: Core Systems
- **Phase 2 (Weeks 3-4)**: Game Features
- **Phase 3 (Weeks 5-6)**: Polish & Launch

## Getting Started

1. Review [Project Setup](docs/implementation/setup/project-setup.md)
2. Install dependencies from [Dependencies](docs/technical/dependencies.md)
3. Configure hardware following [Hardware Setup](docs/technical/hardware/configuration.md)
4. Run development environment

## Contributing

1. Review the [Contributing Guide](docs/meta/contributing.md)
2. Check the [Style Guide](docs/meta/style-guide.md)
3. Follow the [Project Setup Guide](docs/implementation/setup/project-setup.md)

## Documentation

### Overview
- [Project Scope](docs/overview/project-scope.md)
- [System Architecture](docs/overview/system-architecture.md)
- [Research Objectives](docs/overview/research-objectives.md)

### Technical
- [API Specification](docs/technical/api/endpoints.md)
- [Data Schemas](docs/technical/data-schemas/)
- [Hardware Configuration](docs/technical/hardware/configuration.md)

### Implementation
- [Server Architecture](docs/implementation/server/architecture.md)
- [Client Architecture](docs/implementation/client/architecture.md)
- [AI Implementation](docs/implementation/ai/architecture.md)

## License

MIT License - see LICENSE file for details.

## Key Features

- **Edge AI Gaming**: Run sophisticated AI opponents entirely on Raspberry Pi
- **Adaptive Behavior**: AI adapts to player skill and style
- **Hardware Optimized**: Designed for Raspberry Pi 5 with AI HAT+
- **Research Focus**: Explore edge AI capabilities and limitations

## Project Heritage

This project builds upon two previous experimental implementations:
- [golang_turnbased_game_spike](https://github.com/MaterDev/golang_turnbased_game_spike) - A Go/React implementation focusing on real-time battle state updates and frontend integration
- [Simulat33](https://github.com/MaterDev/Python_Jupyter_Experiments/tree/main/projects/06_simulat33) - A Python-based implementation exploring complex battle mechanics and interactive UI

The Path (AI-Pi) combines the technical architecture insights from the Go implementation with the rich battle mechanics of Simulat33, while adding sophisticated edge AI capabilities through dedicated hardware.

## Research

The project explores several key areas:
- Edge AI performance characteristics
- Adaptive gaming AI behavior
- Hardware optimization techniques
- Player interaction patterns

See [research objectives](docs/overview/research-objectives.md) for details.
