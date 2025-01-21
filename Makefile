.PHONY: help install docs docs-build update-logs update-docs clean format lint test setup validate-docs autoformat check-images process-images scrub-images

# Colors for terminal output
COLOR_RESET = \033[0m
COLOR_BOLD = \033[1m
COLOR_GREEN = \033[32m
COLOR_YELLOW = \033[33m
COLOR_BLUE = \033[34m

help:
	@echo "$(COLOR_BLUE)Available commands:$(COLOR_RESET)"
	@echo ""
	@echo "$(COLOR_GREEN)Documentation:$(COLOR_RESET)"
	@echo "  make docs          - Build and serve documentation locally"
	@echo "  make docs-build    - Build documentation site"
	@echo "  make validate-docs - Run documentation validation checks"
	@echo ""
	@echo "$(COLOR_GREEN)Development:$(COLOR_RESET)"
	@echo "  make format       - Format code and documentation"
	@echo "  make lint         - Run linters (auto-fix and verify)"
	@echo "  make test         - Run tests"
	@echo "  make clean        - Clean build artifacts"
	@echo ""
	@echo "$(COLOR_GREEN)Images:$(COLOR_RESET)"
	@echo "  make check-images  - Check images for optimization needs"
	@echo "  make process-images - Optimize images (resize, DPI, metadata)"
	@echo ""
	@echo "$(COLOR_GREEN)Automation:$(COLOR_RESET)"
	@echo "  make update-logs   - Update development logs"
	@echo "  make update-docs   - Update documentation files"

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

# Development
clean:
	@echo "$(COLOR_BLUE)Cleaning build artifacts...$(COLOR_RESET)"
	rm -rf site/
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	@echo "$(COLOR_BLUE)Clean complete$(COLOR_RESET)"

format:
	@echo "$(COLOR_BLUE)Formatting code and documentation...$(COLOR_RESET)"
	@python docs/scripts/doc_validation/format_docs.py
	@ruff check --fix .
	@black .
	@isort .
	@echo "$(COLOR_BLUE)Formatting complete$(COLOR_RESET)"

lint: format
	@echo "$(COLOR_BLUE)Checking code style...$(COLOR_RESET)"
	@ruff check .
	@black . --check
	@isort . --check
	@echo "$(COLOR_BLUE)All checks passed!$(COLOR_RESET)"

test:
	@echo "$(COLOR_BLUE)Running tests...$(COLOR_RESET)"
	pytest

# Documentation
docs:
	@echo "$(COLOR_BLUE)Starting documentation server...$(COLOR_RESET)"
	mkdocs serve

docs-build:
	@echo "$(COLOR_BLUE)Building documentation...$(COLOR_RESET)"
	mkdocs build
	@echo "$(COLOR_BLUE)Documentation built in 'site' directory$(COLOR_RESET)"

validate-docs:
	@echo "$(COLOR_BLUE)Validating documentation...$(COLOR_RESET)"
	@PYTHONPATH=docs/scripts python3 docs/scripts/doc_validation/validate_docs.py docs/
	@echo "$(COLOR_BLUE)Documentation validation complete$(COLOR_RESET)"
	@echo "$(COLOR_BLUE)See /tmp/doc_validation/ for detailed reports$(COLOR_RESET)"

update-logs:
	@echo "$(COLOR_BLUE)Updating development logs...$(COLOR_RESET)"
	@python docs/scripts/log_management/update_logs.py
	@python docs/scripts/log_management/calculate_dev_hours.py
	@echo "$(COLOR_BLUE)Development logs updated$(COLOR_RESET)"

update-docs:
	@echo "$(COLOR_BLUE)Updating documentation...$(COLOR_RESET)"
	@cp docs/scripts/README.md docs/scripts/README.md
	@cp docs/scripts/doc_validation/README.md docs/scripts/doc_validation/README.md
	@echo "$(COLOR_BLUE)Documentation updated$(COLOR_RESET)"

# Images
check-images:
	@echo "$(COLOR_BLUE)Checking images...$(COLOR_RESET)"
	@python docs/scripts/image_management/image_processing.py --directory docs/ --check
	@echo "$(COLOR_BLUE)Image check complete$(COLOR_RESET)"

process-images:
	@echo "$(COLOR_BLUE)Processing images...$(COLOR_RESET)"
	@python docs/scripts/image_management/image_processing.py --directory docs/
	@echo "$(COLOR_BLUE)Image processing complete$(COLOR_RESET)"

scrub-images:
	@echo "$(COLOR_YELLOW)Checking for images with metadata...$(COLOR_RESET)"
	@python docs/scripts/image_management/scrub_metadata.py --directory . --dry-run
	@echo "$(COLOR_YELLOW)Do you want to proceed with removing metadata? [y/N]$(COLOR_RESET)" && read ans && [ $${ans:-N} = y ]
	@echo "$(COLOR_YELLOW)Scrubbing metadata from images...$(COLOR_RESET)"
	@python docs/scripts/image_management/scrub_metadata.py --directory .

# Default target
.DEFAULT_GOAL := help
