# The Path (AI-Pi)

## Overview

The Path (AI-Pi) is a research project exploring edge AI capabilities through a turn-based combat system running on Raspberry Pi hardware. The project demonstrates sophisticated AI behavior running entirely on local hardware, providing unique insights into edge AI gaming.

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

## Documentation

### Overview
- [Project Scope](docs/overview/project-scope.md)
- [System Architecture](docs/overview/system-architecture.md)
- [Research Objectives](docs/overview/research-objectives.md)

### Technical Documentation
- [Data Schemas](docs/technical/data-schemas/)
- [AI System](docs/technical/ai-system/)
- [Hardware](docs/technical/hardware/)

### Implementation Guides
- [Server](docs/implementation/server/architecture.md)
- [Client](docs/implementation/client/architecture.md)
- [Testing](docs/implementation/testing/overview.md)

### Meta Documentation
- [Contributing Guide](docs/meta/contributing.md)
- [Style Guide](docs/meta/style-guide.md)

## Getting Started

1. **Hardware Requirements**
   - Raspberry Pi 5 (8GB recommended)
   - AI HAT+ module
   - Active cooling solution
   - Optional: 7-inch touchscreen

2. **Software Setup**
   ```bash
   # Clone repository
   git clone https://github.com/MaterDev/thepath-ai_pi.git
   cd thepath-ai_pi

   # Install dependencies
   # Server (Go)
   go mod download

   # Client (TypeScript)
   npm install

   # AI System (Python)
   pip install -r requirements.txt
   ```

3. **Configuration**
   - Follow the [hardware configuration guide](docs/technical/hardware/configuration.md)
   - Set up development environment using [contributing guide](docs/meta/contributing.md)
   - Review [system architecture](docs/overview/system-architecture.md)

## Development

- Follow the [style guide](docs/meta/style-guide.md)
- Write tests following [testing guide](docs/implementation/testing/overview.md)
- Submit changes according to [contributing guide](docs/meta/contributing.md)

## Research

The project explores several key areas:
- Edge AI performance characteristics
- Adaptive gaming AI behavior
- Hardware optimization techniques
- Player interaction patterns

See [research objectives](docs/overview/research-objectives.md) for details.

## License

[MIT License](LICENSE)

## Contributing

We welcome contributions! Please see our [contributing guide](docs/meta/contributing.md) for details.
