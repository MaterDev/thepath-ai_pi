---

title: Documentation Scripts Overview
description: Overview of scripts used for managing and validating documentation

---

# Overview of Documentation Scripts

The code for this documentation contains scripts designed to maintain the quality and integrity of the AI-Pi documentation system. These tools automate the processes of validation, logging, and content management to ensure consistency and accuracy across all documentation.

## Requirements

!!! note "Global Dependencies"
    - Python 3.9+

    - Operating System: Linux, macOS, or Windows

    - Git (for version control)

    - Make (for running convenience commands)

Each script category has its own specific dependencies. See their respective README files for details:

- [Image Management](image_management/README.md#requirements)

- [Documentation Validation](doc_validation/README.md#requirements)

- [Log Management](log_management/README.md#requirements)

## Methodology

Our documentation system is built on several key principles:

1. **Automated Validation**: Scripts verify documentation structure, links, and content integrity

2. **Consistent Formatting**: Tools ensure uniform style and presentation

3. **Privacy Protection**: Automated removal of sensitive metadata from AI-generated images

4. **Version Control**: Systematic tracking of documentation changes

## Script Categories

!!! note "Image Management (`image_management/`)"
    Tools for processing and optimizing images in documentation:

    - Metadata removal for privacy protection

    - Web optimization (size and DPI)

    - Format-specific quality settings

    - Automated validation

!!! note "Documentation Validation (`doc_validation/`)"
    Scripts that verify documentation quality:

    - Link checking
    - Format validation
    - Structure verification
    - Content integrity checks
    - Automatic markdown formatting
    - Consistent spacing and style

!!! note "Log Management (`log_management/`)"
    Scripts for managing development logs and tracking progress:

    - `update_logs.py`: Updates documentation navigation with log files

    - `calculate_dev_hours.py`: Tracks total development hours and updates main page

    - Automatically runs during documentation deployment

    - Maintains consistent log format and structure

## Best Practices

1. Run validation scripts before committing changes
2. Always check images for metadata using `make check-images`

3. Keep logs updated with significant changes
4. Follow the established documentation structure

## Getting Started

See individual script directories for detailed usage instructions:

- [Image Management Documentation](image_management/README.md)

- [Documentation Validation Guide](doc_validation/README.md)

- [Log Management Guide](log_management/README.md)
