# Development Scripts

This directory contains utility scripts for managing the project.

## Available Scripts

### `update_logs.py`
Updates the mkdocs.yml navigation with the latest log files.

**Usage:**
```bash
# From the project root:
python scripts/update_logs.py
```

**What it does:**
- Scans the `docs/meta/logs` directory for log files
- Updates mkdocs.yml with the latest files
- Sorts logs by date (newest first)
- Maintains proper formatting and structure

**When to use:**
- After adding new log files
- After removing log files
- When reorganizing the documentation

## Adding New Scripts

When adding new scripts:
1. Add the script to this directory
2. Update this README with usage instructions
3. Make sure the script is executable
4. Add any necessary dependencies to requirements.txt
