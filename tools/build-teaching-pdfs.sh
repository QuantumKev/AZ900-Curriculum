#!/usr/bin/env bash
# Printable PDFs for instructor notes and lab guides.
#
# Usage: bash tools/build-teaching-pdfs.sh
#
# Slide files are left as Markdown so they can be projected.
# Requires the same toolchain as tools/build-pdf.py.

set -euo pipefail
cd "$(dirname "$0")/.."

echo "Building instructor notes..."
for source in sessions/*-instructor-notes.md; do
  python3 tools/build-pdf.py "$source" "${source%.md}.pdf"
done

echo "Building lab guides..."
for source in labs/session-*.md; do
  python3 tools/build-pdf.py "$source" "${source%.md}.pdf"
done

echo
echo "Done. PDFs:"
ls -1 sessions/*-instructor-notes.pdf labs/session-*.pdf
