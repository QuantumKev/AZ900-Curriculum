#!/usr/bin/env python3
"""Render a Markdown file in this repository to a print-ready PDF.

Usage:
    python3 tools/build-pdf.py <input.md> [<output.pdf>]

Requires Python's `markdown` package (`pip install markdown`) and Google Chrome
or Chromium on PATH. Chrome does the PDF printing in headless mode, so the
result matches what you would get from a browser's Print to PDF.
"""

import re
import shutil
import subprocess
import sys
import tempfile
import time
from pathlib import Path

CHROME_CANDIDATES = [
    "google-chrome",
    "chromium",
    "chromium-browser",
    "google-chrome-stable",
]

CSS = """
@page { size: Letter; margin: 18mm 16mm 20mm 16mm; }
@page :first { margin-top: 14mm; }
html { -webkit-print-color-adjust: exact; print-color-adjust: exact; }
body {
  font-family: "Segoe UI", "Helvetica Neue", Arial, sans-serif;
  font-size: 10.5pt; line-height: 1.45; color: #17202a; margin: 0;
}
h1 {
  font-size: 21pt; line-height: 1.2; margin: 0 0 4pt; color: #0b3d63;
  border-bottom: 2.5pt solid #0b3d63; padding-bottom: 5pt;
}
h2 {
  font-size: 13.5pt; margin: 17pt 0 5pt; color: #0b3d63;
  border-bottom: 0.6pt solid #c5d4e0; padding-bottom: 3pt;
  break-after: avoid; page-break-after: avoid;
}
h3 { font-size: 11.5pt; margin: 12pt 0 4pt; color: #1b4f74;
     break-after: avoid; page-break-after: avoid; }
h4 { font-size: 10.5pt; margin: 10pt 0 3pt; color: #1b4f74; }
p, li { orphans: 3; widows: 3; }
p { margin: 0 0 6pt; }
ul, ol { margin: 0 0 7pt; padding-left: 18pt; }
li { margin: 0 0 2.5pt; }
strong { color: #0b3d63; }
a { color: #14568a; text-decoration: none; overflow-wrap: anywhere; }
code {
  font-family: "Cascadia Mono", Consolas, "Liberation Mono", monospace;
  font-size: 9pt; background: #eef3f7; padding: 0.5pt 3pt; border-radius: 2pt;
}
table {
  border-collapse: collapse; width: 100%; margin: 4pt 0 11pt; font-size: 9.2pt;
  break-inside: auto;
}
th, td {
  border: 0.6pt solid #b9c9d6; padding: 3.5pt 5pt; text-align: left;
  vertical-align: top;
}
th { background: #e8eff5; color: #0b3d63; font-weight: 600; }
tr { break-inside: avoid; page-break-inside: avoid; }
blockquote {
  margin: 6pt 0; padding: 5pt 9pt; border-left: 2.5pt solid #0b3d63;
  background: #f4f8fb;
}
hr { border: none; border-top: 0.6pt solid #c5d4e0; margin: 13pt 0; }
.pagebreak { break-before: page; page-break-before: always; }
/* Printable write-on line: <span class="blank"></span> */
.blank {
  display: inline-block; min-width: 2.4in; border-bottom: 0.7pt solid #8296a4;
  height: 1.05em; vertical-align: bottom;
}
.blank-wide { min-width: 4.2in; }
"""

HTML = """<!doctype html>
<html lang="en"><head><meta charset="utf-8"><title>{title}</title>
<style>{css}</style></head><body>{body}</body></html>"""


def find_chrome() -> str:
    for candidate in CHROME_CANDIDATES:
        found = shutil.which(candidate)
        if found:
            return found
    sys.exit("No Chrome or Chromium found on PATH; cannot print to PDF.")


def render(md_path: Path, pdf_path: Path) -> None:
    import markdown

    text = md_path.read_text()
    title = next(
        (line.lstrip("# ").strip() for line in text.splitlines() if line.startswith("# ")),
        md_path.stem,
    )
    # Page-break markers let a source file control pagination in print.
    text = text.replace("<!-- pagebreak -->", '<div class="pagebreak"></div>')
    body = markdown.markdown(
        text, extensions=["tables", "fenced_code", "sane_lists", "attr_list", "md_in_html"]
    )
    # Relative links to repo files mean nothing in a printed handout.
    body = re.sub(r'<a href="(?!https?:|#|mailto:)[^"]*">(.*?)</a>', r"\1", body, flags=re.S)

    with tempfile.TemporaryDirectory() as tmp:
        html_path = Path(tmp) / "doc.html"
        html_path.write_text(HTML.format(title=title, css=CSS, body=body))
        pdf_path.parent.mkdir(parents=True, exist_ok=True)
        if pdf_path.exists():
            pdf_path.unlink()
        process = subprocess.Popen(
            [
                find_chrome(),
                "--headless=new",
                "--disable-gpu",
                "--no-sandbox",
                "--disable-dev-shm-usage",
                f"--user-data-dir={tmp}/profile",
                "--no-pdf-header-footer",
                "--virtual-time-budget=8000",
                f"--print-to-pdf={pdf_path}",
                html_path.as_uri(),
            ],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
        # Headless Chrome writes the PDF and then does not always exit in
        # container environments, so wait for the file to settle and move on.
        try:
            last = -1
            for _ in range(90):
                if process.poll() is not None:
                    break
                size = pdf_path.stat().st_size if pdf_path.exists() else 0
                if size > 0 and size == last:
                    break
                last = size
                time.sleep(1)
        finally:
            if process.poll() is None:
                process.terminate()
                try:
                    process.wait(timeout=10)
                except subprocess.TimeoutExpired:
                    process.kill()

    if not pdf_path.exists() or pdf_path.stat().st_size == 0:
        sys.exit(f"Chrome did not produce a PDF at {pdf_path}")
    print(f"{md_path} -> {pdf_path} ({pdf_path.stat().st_size // 1024} KB)")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    source = Path(sys.argv[1])
    target = Path(sys.argv[2]) if len(sys.argv) > 2 else source.with_suffix(".pdf")
    render(source, target)
