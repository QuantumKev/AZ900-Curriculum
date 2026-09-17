#!/usr/bin/env bash
# Build every printable artifact: syllabus, objective checklist, and quiz handouts.
#
# Usage: bash tools/build-all-pdfs.sh
#
# Requires: python3 with the `markdown` package, and Google Chrome or Chromium
# on PATH. See tools/build-pdf.py.

set -euo pipefail
cd "$(dirname "$0")/.."

echo "Regenerating handouts and the objective checklist..."
python3 tools/export-quizzes.py >/dev/null
python3 tools/build-checklist.py >/dev/null

echo "Building syllabus..."
python3 tools/build-pdf.py syllabus/course-syllabus.md syllabus/course-syllabus.pdf

echo "Building objective checklist..."
python3 tools/build-pdf.py handouts/objective-checklist.md handouts/objective-checklist.pdf

echo "Building quiz handouts..."
for source in handouts/*-handout.md; do
  python3 tools/build-pdf.py "$source" "${source%.md}.pdf"
done

echo
echo "Done. PDFs:"
ls -1 syllabus/*.pdf handouts/*.pdf
