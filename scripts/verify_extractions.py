"""Audit PDF coverage, source hashes, physical pages and full native text.

Requires pypdfium2. This check reads original PDFs independently of extraction
caches, so it can be run after cloning the repository.
"""
from pathlib import Path
import collections, hashlib, json, re
import pypdfium2 as pdfium

root = Path(__file__).resolve().parents[1]
materials = json.loads((root/'metadata/materials.json').read_text(encoding='utf-8'))['files']
expected = {x['id']: x for x in materials if x['format']=='.pdf'}
rows = json.loads((root/'metadata/extractions.json').read_text(encoding='utf-8'))['files']
assert len(rows)==len(expected)
assert {r['id'] for r in rows}==set(expected)
assert len({r['extracted_path'] for r in rows})==len(rows)
descriptions = json.loads((root/'metadata/diagram-descriptions.json').read_text(encoding='utf-8'))
totals = collections.Counter()
for row in rows:
    item = expected[row['id']]
    assert row['source_path']==item['repository_path']
    source = root/row['source_path']
    assert hashlib.sha256(source.read_bytes()).hexdigest()==item['sha256']==row['source_sha256']
    text = (root/row['extracted_path']).read_text(encoding='utf-8')
    assert f'`{row["source_path"]}`' in text
    assert item['sha256'] in text
    # Page headings occur outside fenced source text.
    stripped = re.sub(r'^(`{3,}|~{3,})[^\n]*\n.*?^\1\s*$', '', text, flags=re.M|re.S)
    numbers = [int(x) for x in re.findall(r'^## PDF 第 (\d+) 页$', stripped, re.M)]
    doc = pdfium.PdfDocument(source)
    assert numbers==list(range(1,len(doc)+1)), row['id']+' page sequence'
    assert row['pages']==len(doc)==item['pdf_pages']
    for i in range(len(doc)):
        page=doc[i]; tp=page.get_textpage()
        native=tp.get_text_range().replace('\r\n','\n').replace('\r','\n').replace('\x00','').strip()
        tp.close();page.close()
        if native:
            assert '\n````text\n'+native+'\n````\n' in text, f'{row["id"]} page {i+1} missing native text'
            totals['native_pages_checked']+=1
    for num,desc in descriptions.get(row['id'],{}).items():
        assert 1<=int(num)<=len(doc)
        assert desc in text
        totals['diagram_descriptions']+=1
    doc.close()
    totals['pages']+=row['pages'];totals['files']+=1
    totals['source_files']+=int('/source/' in row['source_path'])
    totals['ocr_pages']+=row.get('ocr_pages',0)
    if totals['files']%50==0: print(f'Checked {totals["files"]}/{len(rows)} PDFs',flush=True)
assert totals['diagram_descriptions']==sum(len(v) for v in descriptions.values())
actual={p.relative_to(root).as_posix() for p in (root/'courses').glob('*/extracted/**/*.pdf.md')}
assert actual=={r['extracted_path'] for r in rows}
print('PASS '+json.dumps(dict(totals)))
