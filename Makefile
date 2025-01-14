.PHONY: help install docs docs-build update-logs clean format lint test setup

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
	@echo ""
	@echo "$(COLOR_GREEN)Development:$(COLOR_RESET)"
	@echo "  make format       - Format code with black"
	@echo "  make lint         - Run linters (flake8)"
	@echo "  make test         - Run tests"
	@echo "  make clean        - Clean build artifacts"

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

docs-build:
	@echo "$(COLOR_YELLOW)Building documentation...$(COLOR_RESET)"
	mkdocs build
	@echo "$(COLOR_BLUE)Documentation built in 'site' directory$(COLOR_RESET)"

update-logs:
	@echo "$(COLOR_YELLOW)Updating development logs...$(COLOR_RESET)"
	python scripts/update_logs.py

# Development
clean:
	@echo "$(COLOR_YELLOW)Cleaning build artifacts...$(COLOR_RESET)"
	rm -rf site/
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete

format:
	@echo "$(COLOR_YELLOW)Formatting code...$(COLOR_RESET)"
	black .

lint:
	@echo "$(COLOR_YELLOW)Running linters...$(COLOR_RESET)"
	flake8 .

test:
	@echo "$(COLOR_YELLOW)Running tests...$(COLOR_RESET)"
	pytest

# Default target
.DEFAULT_GOAL := help
