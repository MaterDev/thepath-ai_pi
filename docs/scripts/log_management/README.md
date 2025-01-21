---

title: Log Management Scripts
description: Tools for managing development logs and updates

---

# Log Management Scripts

This directory contains scripts for managing development logs and social media updates.

## Requirements

!!! note "Dependencies"
    - Python 3.9+

    - PyYAML>=6.0

    - python-frontmatter>=1.0.0

    - Python-Markdown (for admonitions)

    - Operating System: Linux, macOS, or Windows

To install dependencies:

```bash
pip install PyYAML>=6.0 python-frontmatter>=1.0.0 python-markdown

```

## Tools Included

### Log Navigation Manager (`update_logs.py`)

- Updates `mkdocs.yml` with the latest log files

- Maintains chronological ordering of logs

- Ensures proper navigation structure

- Integrates new logs into the documentation

- Handles both development logs and social updates

### MkDocs Log Generator (`gen_logs.py`)

- Automatically builds `log_pages.yml` for MkDocs

- Creates chronological navigation structure

- Excludes index files from generation

- Integrates with MkDocs build process

- Ensures proper date-based organization

### Development Hours Tracker (`calculate_dev_hours.py`)

- Calculates total development hours from log files and updates the main documentation page.

- Scans all log files for `duration_hours` field

- Calculates total development time

- Updates `docs/index.md` with an admonition showing total hours

- Runs automatically during documentation deployment

## Purpose

These tools are essential for maintaining a clear and organized log structure within the documentation, aiding both AI agents and human developers in navigating the project's history and updates.

## Usage

The scripts are typically run through the Makefile:

```bash
make update-logs  # Updates navigation and calculates total development hours

```

## Log File Format

Each log file should include a YAML block with the following fields:

```yaml
type: [Type of work]
duration_hours: [Duration in hours, e.g., 4.5]
hashtags: [comma-separated-tags]

blockers: [Any blockers or None]

```
