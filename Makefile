.PHONY: help install docs docs-build update-logs update-docs clean format lint test setup validate-docs autoformat check-images process-images scrub-images

# Colors for terminal output
COLOR_RESET = \033[0m
COLOR_BOLD = \033[1m
COLOR_GREEN = \033[32m
COLOR_YELLOW = \033[33m
COLOR_BLUE = \033[34m

help:
	@echo "$(COLOR_BOLD)Available commands:$(COLOR_RESET)"
	@echo ""
	@echo "$(COLOR_GREEN)Setup:$(COLOR_RESET)"
	@echo "  make setup        - Initial project setup (dependencies + docs)"
	@echo "  make install      - Install Python dependencies"
	@echo ""
	@echo "$(COLOR_GREEN)Documentation:$(COLOR_RESET)"
	@echo "  make docs         - Start the documentation server"
	@echo "  make docs-build   - Build the documentation site"
	@echo "  make update-logs  - Update development logs in mkdocs.yml"
	@echo "  make update-docs  - Update documentation"
	@echo "  make validate-docs - Run documentation validation checks"
	@echo ""
	@echo "$(COLOR_GREEN)Development:$(COLOR_RESET)"
	@echo "  make format       - Format code with black"
	@echo "  make lint         - Run linters (flake8)"
	@echo "  make test         - Run tests"
	@echo "  make clean        - Clean build artifacts"
	@echo "  make autoformat   - Auto-format Python code"
	@echo "  make check-images - Check for images with metadata"
	@echo "  make process-images - Process images (remove metadata, resize, optimize)"
	@echo "  make scrub-images - Remove metadata from images"

# Initial setup
setup: install docs-deps
	@echo "$(COLOR_BLUE)Project setup complete!$(COLOR_RESET)"
	@echo "$(COLOR_BLUE)Run 'make docs' to start the documentation server$(COLOR_RESET)"

# Install all dependencies
install:
	@echo "$(COLOR_YELLOW)Installing project dependencies...$(COLOR_RESET)"
	pip install -r requirements.txt

# Install documentation dependencies specifically
docs-deps:
	@echo "$(COLOR_YELLOW)Installing documentation dependencies...$(COLOR_RESET)"
	pip install mkdocs-material

# Documentation
docs:
	@echo "$(COLOR_YELLOW)Starting documentation server...$(COLOR_RESET)"
	@echo "$(COLOR_BLUE)Open http://127.0.0.1:8000 in your browser$(COLOR_RESET)"
	mkdocs serve

docs-build: validate-docs
	@echo "$(COLOR_YELLOW)Building documentation...$(COLOR_RESET)"
	mkdocs build
	@echo "$(COLOR_BLUE)Documentation built in 'site' directory$(COLOR_RESET)"

validate-docs:
	@echo "$(COLOR_YELLOW)Validating documentation...$(COLOR_RESET)"
	PYTHONPATH=docs/scripts python3 docs/scripts/doc_validation/validate_docs.py docs/
	@echo "$(COLOR_BLUE)Documentation validation complete$(COLOR_RESET)"
	@echo "$(COLOR_BLUE)See /tmp/doc_validation/ for detailed reports$(COLOR_RESET)"

update-logs:
	@echo "$(COLOR_YELLOW)Updating development logs...$(COLOR_RESET)"
	python docs/scripts/log_management/update_logs.py

update-docs:
	@echo "Updating documentation..."
	@cp README.md docs/index.md
	@cp docs/scripts/README.md docs/scripts/README.md
	@cp docs/scripts/doc_validation/README.md docs/scripts/doc_validation/README.md
	@echo "Documentation updated."

# Development
clean:
	@echo "$(COLOR_YELLOW)Cleaning build artifacts...$(COLOR_RESET)"
	rm -rf site/
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete

format:
	@echo "$(COLOR_YELLOW)Formatting code...$(COLOR_RESET)"
	black .

autoformat:
	@echo "Auto-formatting Python code..."
	@autopep8 --in-place --recursive --max-line-length=100 ./docs/scripts/

lint: autoformat
	@echo "Running linters..."
	flake8 .

test:
	@echo "$(COLOR_YELLOW)Running tests...$(COLOR_RESET)"
	pytest

# Image Processing
.PHONY: check-images process-images

check-images:
	@echo "Checking images for metadata, size, and DPI issues..."
	@PYTHONPATH=docs/scripts python3 docs/scripts/image_management/scrub_metadata.py --check

process-images:
	@echo "Processing all images in the repository..."
	@PYTHONPATH=docs/scripts python3 docs/scripts/image_management/scrub_metadata.py
	@echo "Verifying changes..."
	@PYTHONPATH=docs/scripts python3 docs/scripts/image_management/scrub_metadata.py --check

scrub-images:
	@echo "$(COLOR_YELLOW)Checking for images with metadata...$(COLOR_RESET)"
	@python docs/scripts/image_management/scrub_metadata.py --directory . --dry-run
	@echo "$(COLOR_YELLOW)Do you want to proceed with removing metadata? [y/N]$(COLOR_RESET)" && read ans && [ $${ans:-N} = y ]
	@echo "$(COLOR_YELLOW)Scrubbing metadata from images...$(COLOR_RESET)"
	@python docs/scripts/image_management/scrub_metadata.py --directory .

# Default target
.DEFAULT_GOAL := help
