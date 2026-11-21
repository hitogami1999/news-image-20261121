#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Entry for make.fun bounty news-image-20261121.

Copies the bundled entry.png (a one-page newspaper-style atlas of
Saturday 21 November 2026 world news, designed in Canva) to the output
directory. Standard library only, no network, no timestamps: repeated
runs write byte-identical output.
"""

import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "entry.png")


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dest = os.path.join(out_dir, "entry.png")
    shutil.copyfile(SOURCE, dest)
    print(f"wrote {dest} ({os.path.getsize(dest)} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
