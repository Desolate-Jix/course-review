"""Verify archived source hashes and internal Markdown links. No dependencies."""
from pathlib import Path
from urllib.parse import unquote
import json, hashlib, re, sys

root = Path(__file__).resolve().parents[1]
files = json.loads((root / 'metadata/materials.json').read_text(encoding='utf-8'))['files']
errors = []
for item in files:
    path = root / item['repository_path']
    if not path.is_file():
        errors.append('Missing source: ' + str(path))
    elif hashlib.sha256(path.read_bytes()).hexdigest() != item['sha256']:
        errors.append('Hash mismatch: ' + str(path))
links = 0
docs = [root / 'README.md']
for folder in ['docs', 'interview', 'review-plan', 'courses']:
    docs.extend(p for p in (root / folder).rglob('*.md') if 'source' not in p.relative_to(root).parts)
for path in docs:
    text = path.read_text(encoding='utf-8')
    if 'source:F' in text:
        errors.append('Unresolved source reference: ' + str(path))
    for raw in re.findall(r'\]\(([^\n]+?)\)', text):
        if raw.startswith(('https:', 'http:', '#', 'mailto:')):
            continue
        target = (path.parent / unquote(raw.split('#')[0])).resolve()
        links += 1
        if not target.exists():
            errors.append('Broken link: ' + str(path) + ' -> ' + raw)
if errors:
    print('\n'.join(errors))
    sys.exit(1)
print(f'PASS: {len(files)} source hashes; {len(docs)} Markdown files; {links} internal links.')
