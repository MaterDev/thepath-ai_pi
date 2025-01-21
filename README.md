# The Path (AI-Pi)

Edge AI-powered turn-based combat game running on Raspberry Pi hardware.

![The Path (AI-Pi)](docs/images/cover.png)

📚 [View Documentation](https://materdev.github.io/thepath-ai_pi/)

## Quick Start

```bash
# Install dependencies
pip install -r requirements.txt

# Format and lint code
make format
make lint

# Build documentation
make docs-build

# Start documentation server
make docs
```

## Development

The project uses several tools to maintain code quality:

* `ruff`: Fast Python linter with auto-fix
* `black`: Code formatting
* `isort`: Import sorting

These are configured in `pyproject.toml` with sensible defaults that prioritize productivity.

## Documentation

Documentation is built using MkDocs with Material theme. Key features:

* Automatic formatting
* Link validation
* Image optimization
* Development tracking
* Code style checks

### Documentation Requirements

* Python 3.9+
* MkDocs Material theme
* Python-Markdown extensions
* Pillow for image processing

### Available Commands

```bash
# Documentation
make docs              # Start documentation server
make docs-build        # Build documentation site
make docs-deploy       # Deploy to GitHub Pages
make docs-validate     # Validate documentation

# Code Quality
make format           # Format code with black and isort
make lint            # Lint code with ruff
make check-style     # Check code style without fixing

# Image Management
make check-images    # Check image optimization
make process-images  # Optimize images for web

# Development Logs
make update-logs     # Update development logs
make check-logs      # Validate log format
```

Run `make help` to see all available commands.

## Project Structure

```
.
├── docs/               # Documentation
│   ├── meta/          # Development logs and social updates
│   ├── overview/      # Project overview and objectives
│   ├── scripts/       # Documentation automation
│   ├── technical/     # Technical specifications
│   └── world_building/ # Game world and mechanics
├── requirements.txt    # Python dependencies
└── mkdocs.yml         # Documentation configuration
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run `make format` and `make lint`
5. Submit a pull request

## License

This project is licensed under the terms specified in the LICENSE file.
