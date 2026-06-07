#!/usr/bin/env python3

import json
import sys
import urllib.request
from pathlib import Path


def print_usage():
    print("Usage:")
    print("  python3 download_pypi_linux.py <package_name> <output_directory>")
    sys.exit(1)


if len(sys.argv) != 3:
    print_usage()

PACKAGE = sys.argv[1]
OUTPUT_DIR = Path(sys.argv[2]) / PACKAGE
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

success = []
failed = []

print("=" * 70)
print("PyPI Linux Wheel Downloader")
print("=" * 70)
print(f"Package : {PACKAGE}")
print(f"Output  : {OUTPUT_DIR}")
print()

metadata_url = f"https://pypi.org/pypi/{PACKAGE}/json"

try:
    with urllib.request.urlopen(metadata_url) as response:
        metadata = json.load(response)
except Exception as e:
    print("Failed to fetch package metadata:")
    print(e)
    sys.exit(1)

version = metadata["info"]["version"]
files = metadata["urls"]

# فقط wheelهای لینوکس
linux_wheels = [
    f for f in files
    if f["packagetype"] == "bdist_wheel"
    and (
        "manylinux" in f["filename"]
        or "musllinux" in f["filename"]
    )
]

print(f"Latest Version : {version}")
print(f"Linux Wheels   : {len(linux_wheels)}")
print()

if not linux_wheels:
    print("No Linux wheel files found.")
    sys.exit(0)

total = len(linux_wheels)

for index, wheel in enumerate(linux_wheels, start=1):
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
                    f"{downloaded / (1024 * 1024):.2f} MB / "
                    f"{total_size / (1024 * 1024):.2f} MB "
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

(OUTPUT_DIR / "success.txt").write_text(
    "\n".join(success),
    encoding="utf-8"
)

(OUTPUT_DIR / "failed.txt").write_text(
    "\n".join(failed),
    encoding="utf-8"
)

print()
print("Saved to:")
print(OUTPUT_DIR)
