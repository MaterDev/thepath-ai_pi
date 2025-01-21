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

By removing this metadata, we ensure that:
- No sensitive account information is accidentally shared
- Image generation prompts remain private
- Account security is maintained
- Images can be safely used in public documentation

## Scripts

### scrub_metadata.py

Removes metadata (EXIF, XMP, etc.) from images while preserving image quality. This helps:
- Remove AI service identifiers and account data
- Protect privacy by removing sensitive metadata
- Reduce file sizes
- Ensure consistent image handling

Usage:
```bash
# Check for images with metadata (non-destructive)
python scrub_metadata.py --directory PATH --check

# Show what metadata would be removed (dry run)
python scrub_metadata.py --directory PATH --dry-run

# Remove metadata from all images
python scrub_metadata.py --directory PATH
```

Options:
- `--directory`: Root directory to process (default: current directory)
- `--check`: Only check for metadata and exit with status 1 if found
- `--dry-run`: Show what metadata would be removed without modifying files

The script will:
1. Recursively find all images in the specified directory
2. Check for metadata in each image
3. Remove metadata while preserving image quality (unless in check/dry-run mode)
4. Verify metadata was successfully removed
5. Log results and any errors encountered

Supported formats:
- JPEG/JPG
- PNG
- GIF
- TIFF
- BMP

## Makefile Commands

For convenience, you can use these Makefile commands:

```bash
# Check for images with metadata
make check-images

# Remove metadata (includes confirmation prompt)
make scrub-images

```

## Important Note

Always run `make check-images` before committing new images to ensure no sensitive metadata is accidentally included. This is especially important for images generated using Midjourney, DALL-E, or other AI services.
