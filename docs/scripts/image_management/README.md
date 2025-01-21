---

title: Image Management Scripts
description: Tools for managing and optimizing images in the documentation

---

# Image Management Scripts

This directory contains scripts for managing and optimizing images used in the documentation.

## Requirements

!!! note "Dependencies"
    - Python 3.9+

    - Pillow (PIL) library

    - Operating System: Linux, macOS, or Windows

To install dependencies:

```bash
pip install Pillow>=10.0.0

```

## Purpose

The primary purpose of these tools is to protect privacy and security when using AI-generated images. Many AI image generation services (like Midjourney and DALL-E) embed metadata in images that could potentially:

- Contain account identifiers

- Include API keys or session data

- Reveal prompts used for generation

- Link to personal or organizational accounts

## Image Management

Tools for managing and optimizing images in the documentation.

### Image Processing (`image_processing.py`)

Main script for image optimization and validation:

- Automatic metadata management
- Size optimization
- DPI standardization
- Format validation
- Directory scanning
- Check mode for validation

## Usage

Run via Makefile commands:

```bash
# Check images for optimization needs
make check-images

# Process and optimize images
make process-images
```

Or directly:

```bash
# Check images in a directory
python image_processing.py --directory docs/ --check

# Process images in a directory
python image_processing.py --directory docs/
```

## Integration

The image processing is integrated into the GitHub Actions workflow and runs automatically during deployment:

1. Images are checked for optimization needs
2. Images are processed if needed
3. Changes are committed automatically
4. Documentation is rebuilt with optimized images

## Features

- Metadata Management:
  - Remove sensitive metadata
  - Preserve essential image data
  - Validate metadata removal

- Size Optimization:
  - Automatic resizing
  - DPI standardization
  - Format-specific settings

- Validation:
  - Size checks
  - Format validation
  - DPI verification
  - Metadata scanning

## Configuration

Image processing settings are configured in the script:

- Max image width: 800px
- DPI: 72
- Quality: 95%
- Supported formats: jpg, png, gif

## Makefile Commands

For convenience, you can use these Makefile commands:

```bash

# Check for images needing processing

make check-images

# Process and optimize images (includes confirmation prompt)

make process-images

```

The `process-images` command will:

1. Ask for confirmation before making changes
2. Process all images in the repository:
    * Remove metadata (EXIF, XMP, etc.)

    * Resize to max width 800px (maintaining aspect ratio)

    * Set DPI to 72 for web optimization

    * Optimize quality settings (95% JPEG, optimized PNG)

3. Verify all changes were applied correctly

## Important Note

Always run `make check-images` before committing new images to ensure they meet our standards for:

* Privacy (no metadata)

* Web optimization (correct size and DPI)

* File size (optimized formats)

This is especially important for images generated using Midjourney, DALL-E, or other AI services.
