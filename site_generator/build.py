#!/usr/bin/env python3
import os
import markdown

SRC = 'content'
OUT = 'output'

def ensure_outdir():
    if not os.path.exists(OUT):
        os.mkdir(OUT)

def convert_one(md_path):
    name = os.path.splitext(os.path.basename(md_path))[0]
    with open(md_path, 'r', encoding='utf-8') as f:
        md_text = f.read()
    html_body = markdown.markdown(md_text, extensions=['extra'])
    html = f"""<!DOCTYPE html>
<html><head><meta charset='utf-8'><title>{name}</title></head><body>
{html_body}
<br><hr><a href="index.html">Back to index</a></body></html>"""
    out_file = os.path.join(OUT, f"{name}.html")
    with open(out_file, 'w', encoding='utf-8') as f:
        f.write(html)

def build_site():
    ensure_outdir()
    files = [f for f in os.listdir(SRC) if f.endswith('.md')]
    convert = []
    for f in files:
        convert_one(os.path.join(SRC, f))
        convert.append(os.path.splitext(f)[0])
    index = "<ul>\n" + "\n".join(
        [f'<li><a href="{name}.html">{name}</a></li>' for name in sorted(convert)]
    ) + "\n</ul>"
    with open(os.path.join(OUT, 'index.html'), 'w', encoding='utf-8') as f:
        f.write(f"<!DOCTYPE html><body><h1>My Blog</h1>{index}</body></html>")

if __name__ == '__main__':
    build_site()

