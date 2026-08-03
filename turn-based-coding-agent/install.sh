#!/usr/bin/env bash
set -euo pipefail

usage() {
  echo "Usage: $0 [--force] <skills-directory>" >&2
}

force=0
if [[ "${1:-}" == "--force" ]]; then
  force=1
  shift
fi

if [[ $# -ne 1 ]]; then
  usage
  exit 2
fi

source_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
destination_root="$1"
target="$destination_root/turn-based-coding-agent"

mkdir -p "$destination_root"

if [[ -e "$target" ]]; then
  if [[ $force -ne 1 ]]; then
    echo "Target already exists: $target" >&2
    echo "Use --force to replace it." >&2
    exit 1
  fi
  rm -rf "$target"
fi

mkdir -p "$target"
cp -a "$source_dir"/. "$target"/

echo "Installed turn-based-coding-agent to: $target"
