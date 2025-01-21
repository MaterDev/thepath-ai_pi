# Documentation Validation Package

This package provides a comprehensive set of tools for validating documentation in the agenic context system. It helps maintain documentation quality, consistency, and integrity through automated validation checks.

## Requirements

!!! note "Dependencies"
    - Python 3.9+

    - PyYAML>=6.0

    - Markdown>=3.3

    - Operating System: Linux, macOS, or Windows

To install dependencies:

```bash
pip install PyYAML>=6.0 Markdown>=3.3

```

## Components

### Validation Scripts

- `validate_docs.py`: Main validation script that runs all checks

- `format_docs.py`: Markdown formatting script

- `health_checker.py`: Documentation health checks

- `ref_validator.py`: Link and reference validation

- `validation_types.py`: Shared types and utilities

### Features

- Link checking and validation

- Format validation and auto-formatting

- Structure verification

- Content integrity checks

- Consistent spacing and style

### Code Style

The project uses several tools to maintain code quality:

- `ruff`: Fast Python linter with auto-fix

- `black`: Code formatting

- `isort`: Import sorting

These are configured in `pyproject.toml` with sensible defaults that prioritize productivity over strict enforcement.

## Scripts

### `validate_docs.py`

Validates documentation quality and generates reports:

- Link checking

- Format validation

- Structure verification

- Content integrity checks

- Automatically formats documentation before validation

### `format_docs.py`

Formats markdown files according to project standards:

- Fixes trailing whitespace

- Ensures consistent blank lines

- Fixes list spacing

- Fixes heading spacing

- Fixes code block spacing

- Fixes admonition spacing

## Usage

Run via Makefile commands:

```bash
make validate-docs  # Run all validation checks

make format        # Format code and documentation

make lint          # Verify code style

```

Alternatively, the validation package can be used through the main validation script:

```bash
./validate_docs.py /path/to/docs

```

This will:

- Validate all documentation files in the specified directory

- Generate a detailed report with validation results

- Save the report to the .reports directory with a unique filename based on timestamp and UUID

- Provide a symlink to the latest report for easy access

## Output

The validation process generates two types of output:

1. Human-readable report (`validation_report_TIMESTAMP.txt`)

   - Summary statistics

   - Detailed validation results

   - Issue descriptions and locations

2. JSON results (`validation_results_TIMESTAMP.json`)
   - Raw validation data

   - Detailed statistics

   - Machine-readable format

## Best Practices

1. Run validations before committing documentation changes
2. Review all validation reports carefully
3. Address errors before warnings
4. Keep the style guide updated
5. Monitor documentation health trends

## Implementation Notes

- All validators return `ValidationResult` objects

- Results include both issues and statistics

- Issues are categorized by severity

- File paths are stored relative to docs root

- JSON output preserves all validation details
