---
title: Image Management Scripts
description: Tools for managing and optimizing images in the documentation
---

# Image Management Scripts

This directory contains scripts for managing and optimizing images used in the documentation.

## Purpose

The primary purpose of these tools is to protect privacy and security when using AI-generated images. Many AI image generation services (like Midjourney and DALL-E) embed metadata in images that could potentially:
- Contain account identifiers
- Include API keys or session data
- Reveal prompts used for generation
- Link to personal or organizational accounts

## Image Processing

The scripts automatically process images to ensure:

!!! success "Privacy Protection"
    - Remove all metadata (EXIF, XMP, etc.)
    - Strip AI service identifiers
    - Clean sensitive account data

!!! success "Image Optimization"
    - Set resolution to 72 DPI for web
    - Resize to max width of 800px (maintaining aspect ratio)
    - Optimize file size while preserving quality

!!! success "Format Support"
    - JPEG/JPG (95% quality, optimized)
    - PNG (optimized)
    - GIF
    - TIFF
    - BMP

## Scripts

### scrub_metadata.py

Processes images by removing metadata and optimizing for web use:

Usage:
```bash
# Check for images needing processing (non-destructive)
python scrub_metadata.py --directory PATH --check

# Show what changes would be made (dry run)
python scrub_metadata.py --directory PATH --dry-run

# Process all images
python scrub_metadata.py --directory PATH
```

Options:
- `--directory`: Root directory to process (default: current directory)
- `--check`: Only check for issues and exit with status 1 if found
- `--dry-run`: Show what changes would be made without modifying files

The script will:
1. Recursively find all images in the specified directory
2. Check for metadata and optimization needs
3. Process each image:
   - Remove metadata
   - Set DPI to 72
   - Resize if width > 800px
   - Optimize for web
4. Verify all changes were applied correctly
5. Log results and any errors encountered

## Makefile Commands

For convenience, you can use these Makefile commands:

```bash
# Check for images needing processing
make check-images

# Process images (includes confirmation prompt)
make scrub-images
```

## Important Note

Always run `make check-images` before committing new images to ensure they meet our standards for:
- Privacy (no metadata)
- Web optimization (correct size and DPI)
- File size (optimized formats)

This is especially important for images generated using Midjourney, DALL-E, or other AI services.
