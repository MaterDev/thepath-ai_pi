#!/usr/bin/env python3
"""Update mkdocs.yml with latest log files and social media posts."""

import os
from datetime import datetime
import yaml
from pathlib import Path

def get_dated_files(directory):
    """Get all dated files from a directory."""
    files = []
    
    # Collect all .md files except index.md
    for file in directory.glob("*.md"):
        if file.name != "index.md":
            try:
                # Parse date from filename (YYYY-MM-DD.md)
                date = datetime.strptime(file.stem, "%Y-%m-%d")
                files.append((date, file))
            except ValueError:
                continue
    
    # Sort by date, newest first
    files.sort(key=lambda x: x[0], reverse=True)
    return files

def update_section(config, section_name, base_path):
    """Update a section in the config with dated files."""
    files = get_dated_files(Path(f"docs/{base_path}"))
    
    for section in config["nav"]:
        if isinstance(section, dict) and section_name in section:
            if section_name == "Social Updates":
                # Handle nested LinkedIn section
                linkedin_section = [{"Overview": f"{base_path}/index.md"}]
                for date, file in files:
                    display_date = date.strftime("%B %d, %Y")
                    linkedin_section.append({display_date: f"{base_path}/{file.name}"})
                
                for item in section[section_name]:
                    if isinstance(item, dict) and "LinkedIn" in item:
                        item["LinkedIn"] = linkedin_section
                        break
            else:
                # Handle regular sections (like Logs)
                section_content = [{"Overview": f"{base_path}/index.md"}]
                for date, file in files:
                    display_date = date.strftime("%B %d, %Y")
                    section_content.append({display_date: f"{base_path}/{file.name}"})
                section[section_name] = section_content
            break
    else:
        # If section doesn't exist, create it after Overview
        if section_name == "Social Updates":
            # Handle nested LinkedIn section
            linkedin_section = [{"Overview": f"{base_path}/index.md"}]
            for date, file in files:
                display_date = date.strftime("%B %d, %Y")
                linkedin_section.append({display_date: f"{base_path}/{file.name}"})
            section_content = [{"LinkedIn": linkedin_section}]
        else:
            # Handle regular sections (like Logs)
            section_content = [{"Overview": f"{base_path}/index.md"}]
            for date, file in files:
                display_date = date.strftime("%B %d, %Y")
                section_content.append({display_date: f"{base_path}/{file.name}"})
        
        # Find Overview section index
        for i, section in enumerate(config["nav"]):
            if isinstance(section, dict) and "Overview" in section:
                # Insert section after Overview
                config["nav"].insert(i + 1, {section_name: section_content})
                break

def update_mkdocs():
    """Update mkdocs.yml with latest log files and social media posts."""
    # Read mkdocs.yml
    with open("mkdocs.yml", "r") as f:
        config = yaml.safe_load(f)
    
    # Update Logs section
    update_section(config, "Logs", "meta/logs")
    
    # Update Social Updates section
    update_section(config, "Social Updates", "meta/social/linkedin")
    
    # Write updated config
    with open("mkdocs.yml", "w") as f:
        yaml.dump(config, f, sort_keys=False, allow_unicode=True)

if __name__ == "__main__":
    update_mkdocs()
