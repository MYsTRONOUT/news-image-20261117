"""Entry program for make.fun news-image-20261117 (Python 3.13, stdlib only).

The entry image is the entry.png shipped beside this file; the program
copies it byte-for-byte to $MAKEFUN_OUTPUT_DIR/entry.png (default /output).
No network, no randomness: two runs write identical bytes.

Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import hashlib
import os
import shutil
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SRC = HERE / "entry.png"


def _sha256(path):
    digest = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main():
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    dst = out_dir / "entry.png"
    shutil.copyfile(SRC, dst)
    # The grader runs this program twice and requires identical bytes:
    # refuse to report success if the copy did not land exactly.
    if _sha256(dst) != _sha256(SRC):
        print("entry.png copy mismatch", file=sys.stderr)
        raise SystemExit(1)


if __name__ == "__main__":
    main()
