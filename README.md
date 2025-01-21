# The Path (AI-Pi)

> Edge AI game development on Raspberry Pi hardware

![The Path (AI-Pi)](images/cover-2025.png)

 **[View Documentation](https://materdev.github.io/thepath-ai_pi/)**

## Development

### Prerequisites
- Python 3.11+
- Raspberry Pi 5
- Make

### Setup

```bash
# Install dependencies
make setup

# Run documentation locally
make docs

# Update documentation
make update-docs
```

### Common Tasks

```bash
# Build project
make build

# Run tests
make test

# Clean build artifacts
make clean

# Deploy documentation
make deploy-docs
```

### Documentation Updates

The documentation is automatically updated and deployed via GitHub Actions when changes are pushed to the main branch.

To update locally:
1. Install documentation dependencies: `pip install -r docs/requirements.txt`
2. Run local server: `mkdocs serve`
3. View at: `http://localhost:8000`

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

## Project Structure

```
.
├── docs/               # Documentation
├── scripts/           # Utility scripts
├── src/               # Source code
├── tests/             # Test files
├── Makefile          # Build automation
└── mkdocs.yml        # Documentation config
```

## License

This project is licensed under the Mater Development General Use License (MDGUL) v1.1.

Copyright (c) 2023 Mater Development

The MDGUL allows personal and educational use while restricting commercial use and redistribution. See the [LICENSE](LICENSE) file for full terms.
