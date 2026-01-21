#!/usr/bin/env python
"""Build script for Command documentation using local mkdocs source."""

import sys
from pathlib import Path

# Add local mkdocs source to path
SCRIPT_DIR = Path(__file__).parent.resolve()
MKDOCS_SRC = SCRIPT_DIR / "mkdocs"
sys.path.insert(0, str(MKDOCS_SRC))

from mkdocs.__main__ import cli

if __name__ == "__main__":
    # Default to 'build' if no args provided
    if len(sys.argv) == 1:
        sys.argv.append("build")

    # Run mkdocs CLI from this directory
    cli()
