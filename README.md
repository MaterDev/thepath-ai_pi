# The Path (AI-Pi)

> Edge AI game development on Raspberry Pi hardware

![The Path (AI-Pi)](images/cover.png)

📚 **[View Documentation](https://materdev.github.io/thepath-ai_pi/)**

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
