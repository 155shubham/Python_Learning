# Pathlib

from pathlib import Path

BASE_DIR = Path(**file**).resolve().parent

BOOKS_PATH = BASE_DIR / "data" / "yourfile.txt"

ross-platform

Works automatically on:

Linux
macOS
Windows

without worrying about:

/ vs \\
Rich utilities
path.exists()
path.name
path.suffix
path.parent
