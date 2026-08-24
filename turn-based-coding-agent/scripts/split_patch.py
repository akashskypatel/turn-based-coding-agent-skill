#!/usr/bin/env python3
"""Prepare a deterministic gzip+Base64 patch payload for GitHub connector writes.

The connector safety policy uses <=19 KB UTF-8 content per individual write.
This script:
- hashes the original patch;
- gzip-compresses it deterministically (mtime=0);
- Base64-encodes without line wrapping/newlines;
- hashes the exact encoded stream;
- splits that stream into deterministic fragments no larger than --part-bytes;
- writes checksum/metadata files.

Fragment files contain only their slice of the Base64 ASCII stream and have no
trailing newline. Concatenating them in lexical order must reproduce the exact
encoded stream byte-for-byte.
"""

from __future__ import annotations

import argparse
import base64
import gzip
import hashlib
import json
from pathlib import Path

DEFAULT_PART_BYTES = 19_000


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("patch", type=Path, help="Unified patch to package")
    parser.add_argument("output_dir", type=Path, help="Destination directory")
    parser.add_argument(
        "--part-bytes",
        type=int,
        default=DEFAULT_PART_BYTES,
        help=f"Maximum encoded bytes per fragment (default: {DEFAULT_PART_BYTES})",
    )
    parser.add_argument(
        "--prefix",
        default="change.patch.b64.part-",
        help="Fragment filename prefix",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if args.part_bytes <= 0 or args.part_bytes > DEFAULT_PART_BYTES:
        raise SystemExit(
            f"--part-bytes must be between 1 and {DEFAULT_PART_BYTES} "
            "to preserve the connector safety ceiling"
        )
    if not args.patch.is_file():
        raise SystemExit(f"Patch not found: {args.patch}")

    patch = args.patch.read_bytes()
    compressed = gzip.compress(patch, mtime=0)
    encoded = base64.b64encode(compressed)

    if any(byte in b" \t\r\n" for byte in encoded):
        raise SystemExit("unexpected whitespace in Base64 payload")

    output = args.output_dir
    output.mkdir(parents=True, exist_ok=True)

    for old in output.glob(f"{args.prefix}*"):
        old.unlink()

    count = max(1, (len(encoded) + args.part_bytes - 1) // args.part_bytes)
    width = max(4, len(str(count - 1)))

    for index in range(count):
        start = index * args.part_bytes
        end = start + args.part_bytes
        part = output / f"{args.prefix}{index:0{width}d}"
        payload = encoded[start:end]
        if len(payload) > DEFAULT_PART_BYTES:
            raise SystemExit("fragment exceeds 19 KB safety ceiling")
        part.write_bytes(payload)

    patch_digest = sha256(patch)
    encoded_digest = sha256(encoded)

    (output / "change.patch.sha256").write_text(
        f"{patch_digest}  change.patch\n", encoding="utf-8"
    )
    (output / "change.patch.b64.sha256").write_text(
        f"{encoded_digest}  change.patch.b64\n", encoding="utf-8"
    )
    metadata = {
        "encoding": "gzip+base64",
        "patch_bytes": len(patch),
        "compressed_bytes": len(compressed),
        "encoded_bytes": len(encoded),
        "part_bytes": args.part_bytes,
        "part_count": count,
        "prefix": args.prefix,
        "patch_sha256": patch_digest,
        "encoded_sha256": encoded_digest,
    }
    (output / "change.patch.payload.json").write_text(
        json.dumps(metadata, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )

    print(f"patch_bytes={len(patch)}")
    print(f"compressed_bytes={len(compressed)}")
    print(f"encoded_bytes={len(encoded)}")
    print(f"part_bytes={args.part_bytes}")
    print(f"part_count={count}")
    print(f"patch_sha256={patch_digest}")
    print(f"encoded_sha256={encoded_digest}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
