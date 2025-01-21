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
    - Operating System: Linux, macOS, or Windows

To install dependencies:
```bash
pip install PyYAML>=6.0 python-frontmatter>=1.0.0
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

## Purpose

These tools are essential for maintaining a clear and organized log structure within the documentation, aiding both AI agents and human developers in navigating the project's history and updates.
