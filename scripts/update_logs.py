#!/usr/bin/env python3
"""Update mkdocs.yml with latest log files."""

import os
from datetime import datetime
import yaml
from pathlib import Path

def update_mkdocs():
    """Update mkdocs.yml with latest log files."""
    # Get all log files
    logs_dir = Path("docs/meta/logs")
    log_files = []
    
    # Collect all .md files except index.md
    for file in logs_dir.glob("*.md"):
        if file.name != "index.md":
            try:
                # Parse date from filename (YYYY-MM-DD.md)
                date = datetime.strptime(file.stem, "%Y-%m-%d")
                log_files.append((date, file))
            except ValueError:
                continue
    
    # Sort by date, newest first
    log_files.sort(key=lambda x: x[0], reverse=True)
    
    # Read mkdocs.yml
    with open("mkdocs.yml", "r") as f:
        config = yaml.safe_load(f)
    
    # Update Logs section
    for section in config["nav"]:
        if isinstance(section, dict) and "Logs" in section:
            logs_section = [{"Overview": "meta/logs/index.md"}]
            
            # Add all log files
            for date, file in log_files:
                display_date = date.strftime("%B %d, %Y")
                logs_section.append({display_date: f"meta/logs/{file.name}"})
            
            section["Logs"] = logs_section
            break
    else:
        # If Logs section doesn't exist, create it after Overview
        logs_section = [{"Overview": "meta/logs/index.md"}]
        for date, file in log_files:
            display_date = date.strftime("%B %d, %Y")
            logs_section.append({display_date: f"meta/logs/{file.name}"})
        
        # Find Overview section index
        for i, section in enumerate(config["nav"]):
            if isinstance(section, dict) and "Overview" in section:
                # Insert Logs section after Overview
                config["nav"].insert(i + 1, {"Logs": logs_section})
                break
    
    # Write updated config
    with open("mkdocs.yml", "w") as f:
        yaml.dump(config, f, sort_keys=False, allow_unicode=True)

if __name__ == "__main__":
    update_mkdocs()
