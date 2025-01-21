# The Path (AI-Pi)

![The Path (AI-Pi)](images/cover-2025.png)

Edge AI-powered turn-based combat game running on Raspberry Pi hardware.

## Getting Started

### Prerequisites

- Python 3.11 or higher
- pip (Python package installer)
- Raspberry Pi 5 (for deployment)

### Development Setup

1. Clone the repository:
```bash
git clone https://github.com/MaterDev/thepath-ai_pi.git
cd thepath-ai_pi
```

2. Run the setup command to install dependencies and initialize the project:
```bash
make setup
```

3. Start the documentation server:
```bash
make docs
```

View the documentation at http://127.0.0.1:8000 for:
- Project overview and architecture
- Technical specifications
- Development guides
- API documentation
- World building and game mechanics

### Development Workflow

Run `make help` to see all available commands for development, testing, and documentation.

Common workflows:
1. Before committing changes:
   ```bash
   make format     # Format code with black
   make autoformat # Auto-fix common Python style issues with autopep8
   make lint       # Check for issues (runs autoformat first)
   make test      # Run tests
   ```
   Note: If the linter finds no issues, it will exit with code 0 and display no output.

2. Working with documentation:
   ```bash
   make validate-docs  # Validate documentation quality
   make docs          # Start documentation server
   make update-logs   # Update mkdocs.yml with latest logs and social posts
   ```
   The `update-logs` command uses two scripts:
   - `update_logs.py`: Updates mkdocs.yml with latest log files and social media posts
   - `gen_logs.py`: Helper script to generate new log entries with consistent formatting

## Project Origins

This project represents the evolution of turn-based battle mechanics through several research spikes:

1. [Simulat33](https://github.com/MaterDev/Python_Jupyter_Experiments/tree/main/projects/06_simulat33) - The initial prototype built in Python using Jupyter notebooks, which established core concepts for:
   - Character class systems with unique abilities
   - Turn-based combat mechanics
   - Interactive battle UI using ipywidgets
   - Status effects and buff systems

2. [huMon-gen](https://github.com/MaterDev/Python_Jupyter_Experiments/tree/main/projects/08_huMon-gen) - A specialized tool for character stat generation and balancing:
   - Algorithmic generation of character stats using ancestral tree patterns
   - Interactive visualization of stat distributions across character generations
   - Comparative analysis tools for balancing character attributes
   - The base character stats used in this project were generated using this system

3. [golang_turnbased_game_spike](https://github.com/MaterDev/golang_turnbased_game_spike) - A Go-based implementation that refined these concepts and added:
   - RESTful API architecture
   - Modern React TypeScript frontend
   - Improved battle state management
   - Enhanced cooldown mechanics

The current project builds upon these previous implementations, incorporating:
- Core battle mechanics from Simulat33
- Balanced character stats generated through huMon-gen
- Modern architecture and UI patterns from the Go implementation

## License

This project is licensed under the Mater Development General Use License (MDGUL) v1.1.

Copyright (c) Mater Development

The MDGUL allows personal and educational use while restricting commercial use and redistribution. See the [LICENSE](LICENSE) file for full terms.
