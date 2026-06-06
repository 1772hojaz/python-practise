#!/bin/python3
# convert_heic_to_png.py
#
# Requirements:
#   pip install pillow pillow-heif
#
# Usage:
#   python convert_heic_to_png.py input.heic
#   python convert_heic_to_png.py /path/to/folder

from pathlib import Path
from PIL import Image
import pillow_heif
import sys

# Enable HEIC support in Pillow
pillow_heif.register_heif_opener()


def convert_heic_to_png(file_path):
    """Convert a single HEIC file to PNG"""
    file_path = Path(file_path)  # Convert to Path object

    # Check if it's a HEIC/HEIF file
    if file_path.suffix.lower() not in [".heic", ".heif"]:
        print(f"Skipping non-HEIC file: {file_path.name}")
        return

    output_path = file_path.with_suffix(".png")

    try:
        with Image.open(file_path) as img:
            img.save(output_path, "PNG")
        print(f"✅ Converted: {file_path.name} -> {output_path.name}")
    except Exception as e:
        print(f"❌ Failed to convert {file_path.name}: {e}")


def process_path(path_str):
    """Process either a single file or all HEIC files in a directory"""
    path = Path(path_str)

    if path.is_file():
        convert_heic_to_png(path)
    elif path.is_dir():
        heic_files = list(path.glob("*.heic")) + list(path.glob("*.HEIC")) + \
                     list(path.glob("*.heif")) + list(path.glob("*.HEIF"))
        
        if not heic_files:
            print(f"No HEIC/HEIF files found in {path}")
            return
        
        for file in heic_files:
            convert_heic_to_png(file)
    else:
        print(f"❌ Invalid path: {path_str}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python convert_heic_to_png.py input.heic")
        print("  python convert_heic_to_png.py /path/to/folder")
        sys.exit(1)

    process_path(sys.argv[1])
