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

### Documentation Management and Validation

Our documentation system includes a robust validation suite to ensure quality and consistency. Key features include:

- **Metadata Validation**: Checks for required metadata fields like `title` and `description`.
- **Reference Validation**: Verifies all cross-references and links are intact.
- **Report Generation**: Generates detailed reports with unique filenames based on timestamp and UUID, providing a symlink to the latest report for easy access.

To run the validation suite:

```bash
make validate-docs
```

Reports are saved in the `.reports` directory, with the latest report symlinked as `latest.json`.

### Documentation Updates

The documentation is automatically updated and deployed via GitHub Actions when changes are pushed to the main branch.

To update locally:
1. Install documentation dependencies: `pip install -r docs/requirements.txt`
2. Run local server: `mkdocs serve`

## Makefile Targets

The following Makefile targets are available for development and maintenance:

### Setup and Installation
- `make setup` - Initial project setup (installs dependencies and documentation tools)
- `make install` - Install Python dependencies from requirements.txt
- `make docs-deps` - Install documentation-specific dependencies

### Documentation
- `make docs` - Start the documentation server (http://127.0.0.1:8000)
- `make docs-build` - Build the documentation site (outputs to 'site' directory)
- `make validate-docs` - Run documentation validation checks
- `make update-logs` - Update development logs in mkdocs.yml
- `make update-docs` - Update documentation by copying README files to appropriate locations

### Development Tools
- `make format` - Format code using black
- `make lint` - Run linters (flake8)
- `make test` - Run pytest test suite
- `make clean` - Clean build artifacts and cache files

### Viewing Documentation

After starting the documentation server with `make docs`, you can view the documentation at http://127.0.0.1:8000.

The documentation includes:
- Project overview and architecture
- Technical specifications
- Development guides
- API documentation
- World building and game mechanics

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

Copyright (c) 2023 Mater Development

The MDGUL allows personal and educational use while restricting commercial use and redistribution. See the [LICENSE](LICENSE) file for full terms.
