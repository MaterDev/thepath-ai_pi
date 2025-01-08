# The Path (AI-Pi)

A research project exploring personalized AI opponents in gaming through edge computing. Using the Raspberry Pi platform and AI HAT+ hardware, this project aims to create engaging AI opponents that learn and adapt to each player's style - all while running locally on affordable hardware.

## Project Overview

The Path (AI-Pi) investigates how dedicated AI hardware can enable sophisticated, personalized gaming experiences without cloud dependencies. By combining edge AI processing with rich turn-based combat mechanics, the project creates AI opponents that evolve through gameplay while maintaining the responsiveness and privacy benefits of local processing.

## Research Focus

- **Edge AI Gaming**: Exploring how dedicated AI hardware can enable sophisticated gaming experiences without cloud dependencies
- **Adaptive Difficulty**: Creating AI opponents that naturally adjust to player skill levels
- **Learning from Play**: Collecting and analyzing gameplay data to improve AI behavior over time
- **Hardware Optimization**: Maximizing AI performance on resource-constrained edge devices

## Key Features

- Edge AI processing using Raspberry Pi 5 and AI HAT+
- Sophisticated turn-based combat system featuring:
  - Strategic class-based character system
  - Complex buff/debuff mechanics
  - Probability-based turn order influenced by speed
  - Comprehensive status effect system
- Adaptive AI opponents with configurable difficulty levels
- Local gameplay data collection and analysis
- Research-focused architecture for AI behavior study

## Project Status

This is an active research project investigating the potential of edge AI in gaming. The project aims to demonstrate that sophisticated AI opponents can run effectively on accessible hardware, opening new possibilities for AI integration in games.

## Project Heritage

This project builds upon two previous experimental implementations:
- [golang_turnbased_game_spike](https://github.com/MaterDev/golang_turnbased_game_spike) - A Go/React implementation focusing on real-time battle state updates and frontend integration
- [Simulat33](https://github.com/MaterDev/Python_Jupyter_Experiments/tree/main/projects/06_simulat33) - A Python-based implementation exploring complex battle mechanics and interactive UI

The Path (AI-Pi) combines the technical architecture insights from the Go implementation with the rich battle mechanics of Simulat33, while adding sophisticated edge AI capabilities through dedicated hardware.

## Documentation

The project's detailed documentation is maintained in the `docs` directory:

- [`mvp-scope.md`](docs/mvp-scope.md) - Detailed project roadmap and implementation timeline, including core features and AI system specifications
- [`game-design-document.md`](docs/game-design-document.md) - Comprehensive game mechanics, combat system, and player interaction design
- [`ai-behavior-research.md`](docs/ai-behavior-research.md) - Research findings and implementation details for the AI behavior system
- [`ai-specifications.md`](docs/ai-specifications.md) - Technical specifications for the AI system, including training data structure and reward calculations
- [`hardware-specifications.md`](docs/hardware-specifications.md) - Detailed hardware requirements and configuration for the Raspberry Pi 5 and AI HAT+
- [`data-schema.md`](docs/data-schema.md) - Database schemas and data structures for game state, replays, and AI training

See the [`docs/README.md`](docs/README.md) for an overview of how these documents work together.

## License

This project is licensed under the Mater Development General Use License (MDGUL) v1.1. This is a custom license that allows for personal and educational use while requiring explicit permission for commercial use, redistribution, or creation of derivative works. See the [LICENSE](LICENSE) file for the full terms.

## Acknowledgments

This project is being developed with assistance from:
- Codeium - AI-powered code completion and analysis
- Windsurf - The world's first agentic IDE
