# The Path (AI-Pi)

Edge AI-powered turn-based combat game running on Raspberry Pi hardware.

![The Path (AI-Pi)](images/cover.png)

## Documentation

The documentation is built using MkDocs and includes:

- Project overview and architecture
- Technical specifications
- Development guides
- Implementation details
- World building and game design

For tools that help maintain and validate the documentation, see the [Scripts Documentation](docs/scripts/README.md). These tools handle tasks like:
- Image optimization and privacy protection
- Documentation validation
- Log management

 **[View Full Documentation](https://materdev.github.io/thepath-ai_pi/)**

Our comprehensive documentation site contains everything you need to understand and contribute to the project:
- Technical specifications and architecture
- Development guides and setup instructions
- Game mechanics and world building
- API documentation
- Development logs and updates

## Development

### Quick Start

1. Clone the repository
2. Run `make install` to set up dependencies
3. Run `make docs` to build and serve documentation locally

### Makefile Commands

The project includes a comprehensive Makefile to automate common tasks:

#### Documentation Commands
```
make docs          # Build and serve documentation locally
make docs-build    # Build documentation site
make validate-docs # Run documentation validation
make process-images # Optimize images (resize, set DPI, remove metadata)
make check-images  # Check images for optimization needs
```

#### Development Commands
```
make install      # Install project dependencies
make test        # Run test suite
make lint        # Run linting checks
make format      # Format code
make clean       # Clean build artifacts
```

#### Automation Commands
```
make update-logs  # Update development logs
make update-docs  # Update documentation navigation
```

For detailed information about documentation tools and scripts, see the [Scripts Documentation](docs/scripts/README.md).

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

## Image Assets

This project uses AI-generated images from Midjourney and DALL-E. To protect privacy and security:

1. All images are automatically checked for metadata using `make check-images`
2. Metadata is removed using `make scrub-images` to prevent accidental sharing of:
   - Account identifiers
   - API keys
   - Generation prompts
   - Service-specific data

Always run these commands before committing new images.

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
