#!/usr/bin/env python3

import json
import sys
import urllib.request
from pathlib import Path
from urllib.parse import urlparse

PACKAGE = sys.argv[1] if len(sys.argv) > 1 else None
OUTPUT_DIR = Path(sys.argv[2]) if len(sys.argv) > 2 else None

if not PACKAGE or not OUTPUT_DIR:
    print("Usage:")
    print("  python download_all_wheels.py <package> <output_dir>")
    sys.exit(1)

OUTPUT_DIR = OUTPUT_DIR / PACKAGE
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

success = []
failed = []

print(f"Package: {PACKAGE}")
print(f"Output : {OUTPUT_DIR}")
print()

# دریافت متادیتای پکیج از PyPI
metadata_url = f"https://pypi.org/pypi/{PACKAGE}/json"

try:
    with urllib.request.urlopen(metadata_url) as response:
        metadata = json.load(response)
except Exception as e:
    print(f"Failed to fetch package metadata: {e}")
    sys.exit(1)

version = metadata["info"]["version"]
files = metadata["urls"]

# فقط wheelها
wheels = [f for f in files if f["packagetype"] == "bdist_wheel"]

if not wheels:
    print("No wheel files found.")
    sys.exit(0)

print(f"Latest version : {version}")
print(f"Wheel files    : {len(wheels)}")
print()

total = len(wheels)

for index, wheel in enumerate(wheels, start=1):
    filename = wheel["filename"]
    url = wheel["url"]
    size = wheel["size"]

    destination = OUTPUT_DIR / filename

    print("=" * 70)
    print(f"[{index}/{total}]")
    print(f"File : {filename}")
    print(f"Size : {size / (1024 * 1024):.2f} MB")

    try:
        def progress(blocks, block_size, total_size):
            downloaded = blocks * block_size

            if total_size > 0:
                percent = min(downloaded * 100 / total_size, 100)
                print(
                    f"\rDownloaded: "
                    f"{downloaded / (1024*1024):.2f} MB / "
                    f"{total_size / (1024*1024):.2f} MB "
                    f"({percent:.1f}%)",
                    end="",
                    flush=True
                )

        urllib.request.urlretrieve(
            url,
            destination,
            reporthook=progress
        )

        print("\n✓ SUCCESS")
        success.append(filename)

    except Exception as e:
        print(f"\n✗ FAILED: {e}")
        failed.append(filename)

print()
print("=" * 70)
print("DOWNLOAD COMPLETED")
print("=" * 70)

print(f"Succeeded : {len(success)}")
print(f"Failed    : {len(failed)}")

(Path(OUTPUT_DIR) / "success.txt").write_text(
    "\n".join(success),
    encoding="utf-8"
)

(Path(OUTPUT_DIR) / "failed.txt").write_text(
    "\n".join(failed),
    encoding="utf-8"
)

print()
print("Saved to:")
print(OUTPUT_DIR)

