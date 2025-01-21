#!/usr/bin/env python3
"""Image metadata scrubbing script.

This script removes metadata (EXIF, XMP, etc.) from all images in the repository
while preserving the image content. It supports common image formats including:
- JPEG/JPG
- PNG
- GIF
- TIFF
"""

import os
from pathlib import Path
import argparse
from PIL import Image, ExifTags
import logging
import sys
from typing import Dict, List, Set, Tuple

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class ImageMetadata:
    """Class to handle image metadata operations."""
    
    def __init__(self, image_path: Path):
        """Initialize with image path."""
        self.path = image_path
        self.metadata = {}
        self._load_metadata()
    
    def _load_metadata(self):
        """Load all available metadata from image."""
        try:
            with Image.open(self.path) as img:
                # Get EXIF data
                if hasattr(img, '_getexif') and img._getexif():
                    exif = img._getexif()
                    if exif:
                        for tag_id in exif:
                            try:
                                tag = ExifTags.TAGS.get(tag_id, tag_id)
                                self.metadata[f'EXIF_{tag}'] = str(exif[tag_id])
                            except Exception:
                                continue
                
                # Get other image info
                self.metadata['FORMAT'] = img.format
                self.metadata['MODE'] = img.mode
                self.metadata['SIZE'] = img.size
                
                # Get all available info
                for k, v in img.info.items():
                    if isinstance(v, (str, int, float)):
                        self.metadata[k] = v
        
        except Exception as e:
            logger.error(f"Error loading metadata from {self.path}: {str(e)}")
    
    def has_metadata(self) -> bool:
        """Check if image has any metadata beyond basic format info."""
        basic_info = {'FORMAT', 'MODE', 'SIZE'}
        return len(set(self.metadata.keys()) - basic_info) > 0
    
    def get_metadata_summary(self) -> str:
        """Get a formatted summary of metadata."""
        if not self.has_metadata():
            return "No metadata found"
        
        summary = []
        for k, v in self.metadata.items():
            if k not in {'FORMAT', 'MODE', 'SIZE'}:
                summary.append(f"{k}: {v}")
        return "\n".join(summary)

def get_image_files(directory: Path) -> List[Path]:
    """Find all image files in the directory recursively.
    
    Args:
        directory: Root directory to search
        
    Returns:
        List of paths to image files
    """
    image_extensions = {'.jpg', '.jpeg', '.png', '.gif', '.tiff', '.bmp'}
    image_files = []
    
    for ext in image_extensions:
        image_files.extend(directory.rglob(f'*{ext}'))
        image_files.extend(directory.rglob(f'*{ext.upper()}'))
    
    return sorted(image_files)

def check_images(image_files: List[Path]) -> Tuple[List[Path], List[Path]]:
    """Check which images have metadata.
    
    Args:
        image_files: List of image paths to check
        
    Returns:
        Tuple of (images with metadata, images without metadata)
    """
    with_metadata = []
    without_metadata = []
    
    for path in image_files:
        metadata = ImageMetadata(path)
        if metadata.has_metadata():
            with_metadata.append(path)
        else:
            without_metadata.append(path)
            
    return with_metadata, without_metadata

def scrub_metadata(image_path: Path, dry_run: bool = False) -> bool:
    """Remove metadata from an image file.
    
    Args:
        image_path: Path to the image file
        dry_run: If True, only check for metadata without modifying
        
    Returns:
        True if successful, False if failed
    """
    try:
        metadata = ImageMetadata(image_path)
        
        if dry_run:
            if metadata.has_metadata():
                logger.info(f"Found metadata in {image_path}:")
                logger.info(metadata.get_metadata_summary())
            return True
        
        # Only process if metadata exists
        if not metadata.has_metadata():
            logger.info(f"No metadata to remove from {image_path}")
            return True
        
        # Open image and create a new one without metadata
        with Image.open(image_path) as img:
            # Create a new image with same content but no metadata
            data = list(img.getdata())
            image_without_exif = Image.new(img.mode, img.size)
            image_without_exif.putdata(data)
            
            # Save with optimal settings for each format
            save_kwargs = {}
            if image_path.suffix.lower() in {'.jpg', '.jpeg'}:
                save_kwargs = {'quality': 95, 'optimize': True}
            elif image_path.suffix.lower() == '.png':
                save_kwargs = {'optimize': True}
            
            # Save back to original file
            image_without_exif.save(image_path, **save_kwargs)
            
            # Verify metadata was removed
            check_metadata = ImageMetadata(image_path)
            if check_metadata.has_metadata():
                logger.error(f"Failed to remove all metadata from {image_path}")
                return False
                
            logger.info(f"Successfully scrubbed metadata from {image_path}")
            return True
            
    except Exception as e:
        logger.error(f"Failed to process {image_path}: {str(e)}")
        return False

def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="Remove metadata from images in the repository"
    )
    parser.add_argument(
        "--directory",
        type=str,
        default=".",
        help="Root directory to process (default: current directory)"
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Check for metadata without modifying files"
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="Only check if any images have metadata and exit with status 1 if found"
    )
    args = parser.parse_args()
    
    root_dir = Path(args.directory).resolve()
    if not root_dir.exists():
        logger.error(f"Directory not found: {root_dir}")
        sys.exit(1)
    
    logger.info(f"Searching for images in {root_dir}")
    image_files = get_image_files(root_dir)
    
    if not image_files:
        logger.info("No image files found")
        sys.exit(0)
    
    logger.info(f"Found {len(image_files)} image files")
    
    # Check which images have metadata
    with_metadata, without_metadata = check_images(image_files)
    
    if args.check:
        if with_metadata:
            logger.error(f"Found {len(with_metadata)} images with metadata:")
            for path in with_metadata:
                logger.error(f"  {path}")
            sys.exit(1)
        logger.info("No images with metadata found")
        sys.exit(0)
    
    if not with_metadata:
        logger.info("No images with metadata found")
        sys.exit(0)
    
    logger.info(f"Found {len(with_metadata)} images with metadata")
    
    if args.dry_run:
        for path in with_metadata:
            scrub_metadata(path, dry_run=True)
        sys.exit(0)
    
    # Process each image
    success_count = 0
    for image_path in with_metadata:
        if scrub_metadata(image_path):
            success_count += 1
    
    # Print summary
    logger.info(f"Successfully processed {success_count} of {len(with_metadata)} images")
    
    # Exit with error if any images failed
    if success_count < len(with_metadata):
        sys.exit(1)

if __name__ == "__main__":
    main()
