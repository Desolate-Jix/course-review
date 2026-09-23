"""Page-preserving local PDF extraction. Source files are read only.

Requires pypdfium2 and pypdf. Run prepare, Windows OCR, then build. Intermediate page
records and rendered OCR inputs stay in ignored tmp/course_extract/.
"""
from pathlib import Path
from urllib.parse import quote
import argparse, collections, hashlib, json, logging, os, re
import pypdfium2 as pdfium
from pypdf import PdfReader
logging.getLogger("pypdf").setLevel(logging.ERROR)

ROOT = Path(__file__).resolve().parents[1]
WORK = ROOT / 'tmp/course_extract'
FILES = json.loads((ROOT/'metadata/materials.json').read_text(encoding='utf-8'))['files']
PDFS = [x for x in FILES if x['format']=='.pdf']

def save(path, obj):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, ensure_ascii=False, indent=2), encoding='utf-8')

def tidy(text):
    return text.replace('\r\n','\n').replace('\r','\n').replace('\x00','').strip()

def suspicious(text):
    n=max(1,len(text))
    return (sum(0x80<=ord(c)<0x250 for c in text)/n>0.07
        or sum(ord(c)<32 and c not in '\n\r\t' for c in text)/n>0.01
        or '\ufffd' in text or '\ue000'<=next((c for c in text if '\ue000'<=c<='\uf8ff'),' ')<='\uf8ff')

def prepare():
    (WORK/'pages').mkdir(parents=True,exist_ok=True)
    manifest=[]; stats=collections.Counter()
    for k,item in enumerate(PDFS,1):
        cache=WORK/'pages'/(item['id']+'.json')
        if cache.exists():
            rec=json.loads(cache.read_text(encoding='utf-8'))
            manifest.extend(rec['ocr_jobs']);stats['pages']+=len(rec['pages'])
            continue
        path=ROOT/item['repository_path']
        if hashlib.sha256(path.read_bytes()).hexdigest()!=item['sha256']: raise ValueError('Source changed: '+str(path))
        doc=pdfium.PdfDocument(path)
        pages=[]; jobs=[]
        for j in range(len(doc)):
            page=doc[j]; tp=page.get_textpage(); raw=tidy(tp.get_text_range())
            width,height=page.get_size(); image_area=0; image_count=0; paths=0
            try:
                for obj in page.get_objects():
                    if obj.type==3:
                        image_count+=1
                        l,b,r,t=obj.get_bounds();image_area+=max(0,r-l)*max(0,t-b)
                    elif obj.type==2: paths+=1
            except Exception: pass
            coverage=min(1,image_area/max(1,width*height))
            bad=suspicious(raw)
            need_ocr=len(raw)<140 or bad or coverage>0.16
            record={'page':j+1,'native_text':raw,
                'suspect_encoding':bad,'image_coverage':round(coverage,3),'image_count':image_count,'vector_paths':paths,'ocr_requested':need_ocr}
            tp.close()
            if need_ocr:
                stem=f"{item['id']}_p{j+1:04}"
                imagepath=WORK/'images'/(stem+'.png'); imagepath.parent.mkdir(exist_ok=True)
                page.render(scale=min(3.0,2400/max(width,height))).to_pil().convert('RGB').save(imagepath)
                output=WORK/'ocr'/(stem+'.json'); output.parent.mkdir(exist_ok=True)
                jobs.append({'image':str(imagepath),'output':str(output),'chinese':bool(re.search('[\u4e00-\u9fff]',raw)) or (item['category']=='original-note' and len(raw)<200)})
            pages.append(record); page.close()
        doc.close()
        rec={'item':item,'pages':pages,'ocr_jobs':jobs};save(cache,rec);manifest.extend(jobs)
        stats['pages']+=len(pages)
        if k%10==0: print(f'PREPARE {k}/{len(PDFS)} documents; {stats["pages"]} pages',flush=True)
    save(WORK/'ocr_manifest.json',manifest)
    print(f'PREPARED {len(PDFS)} PDFs, {stats["pages"]} pages, {len(manifest)} OCR pages',flush=True)

def rel_link(target, folder):
    return quote(os.path.relpath(target,folder).replace('\\','/'),safe='/')

def build():
    descriptions_path=ROOT/'metadata/diagram-descriptions.json'
    descriptions=json.loads(descriptions_path.read_text(encoding='utf-8')) if descriptions_path.exists() else {}
    records=[]
    for item in PDFS:
        rec=json.loads((WORK/'pages'/(item['id']+'.json')).read_text(encoding='utf-8'))
        src=Path(item['repository_path']); section='source' if '/source/' in src.as_posix() else 'notes'
        relative=src.as_posix().split('/source/',1)[1] if section=='source' else src.as_posix().split('/notes/original/',1)[1]
        dest=ROOT/'courses'/item['course']/'extracted'/section/(relative+'.md')
        dest.parent.mkdir(parents=True,exist_ok=True)
        origin=rel_link(ROOT/src,dest.parent)
        lines=[f'# {Path(relative).name} — 逐页文本副本','',f'- source 原文件路径：`{src.as_posix()}`',f'- [打开原文件]({origin})',
            f'- 原文件 SHA-256：`{item["sha256"]}`',f'- 文件索引：{item["id"]}；PDF 总页数：{len(rec["pages"])}',
            '- 页码采用 PDF 物理页码。原幻灯片编号作为原文保留，可能与物理页码不同。',
            '- 此文件是原文提取，不是摘要。保留文字层全文；按需附坐标排版及本地 OCR。两种视图可能重复。',
            '- OCR、数学符号和空间布局不保证完全准确；图示说明是另行标注的辅助文字，原 PDF 为准。','']
        stats=collections.Counter()
        layout_reader=PdfReader(ROOT/src) if section=='source' else None
        for p in rec['pages']:
            num=p['page']; stats['pages']+=1
            lines += [f'## PDF 第 {num} 页','',f'[查看此页]({origin}#page={num})','']
            raw=p['native_text']
            if raw:
                lines+=['### 原始文字层','', '````text',raw,'````','']
                stats['native_pages']+=1
                if p['suspect_encoding']:lines+=['> 文字层存在可疑字体映射／乱码；下方 OCR 可辅助对照。原始字符仍保留。','']
                layout=tidy(layout_reader.pages[num-1].extract_text(extraction_mode='layout',layout_mode_space_vertically=False)) if layout_reader and len(raw)>80 and not p['suspect_encoding'] else ''
                if layout:
                    lines+=['### 坐标排版辅助视图','', '> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。','', '````text',layout,'````','']
                    stats['layout_pages']+=1
            else: lines+=['> 本页无可提取文字层；见 OCR 或图示说明。','']
            if p['ocr_requested']:
                op=WORK/'ocr'/f"{item['id']}_p{num:04}.json"
                if not op.exists(): raise ValueError('Missing OCR result '+str(op))
                ocr=json.loads(op.read_text(encoding='utf-8'))
                if ocr.get('error'):raise ValueError('OCR error '+str(op))
                stats['ocr_pages']+=1
                for lang, result in ocr['results'].items():
                    text=tidy(result.get('text',''))
                    if text:lines += [f'### 图片文字 OCR（{lang}，待对照原页）','', '````text',text,'````','']
                if not any(tidy(r.get('text','')) for r in ocr['results'].values()):
                    lines+=['> OCR 未识别出可靠文字；本页可能以图形、手写公式或空白为主。',''];stats['ocr_empty_pages']+=1
            desc=descriptions.get(item['id'],{}).get(str(num))
            if desc:
                lines+=['### 图表辅助说明','',desc,''];stats['described_pages']+=1
            if (p['image_count'] or p['vector_paths']>5) and not desc:
                lines+=['> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。','']
        dest.write_text('\n'.join(lines)+'\n',encoding='utf-8')
        records.append({'id':item['id'],'course':item['course'],'source_path':src.as_posix(),'source_sha256':item['sha256'],'extracted_path':dest.relative_to(ROOT).as_posix(),**dict(stats)})
    save(ROOT/'metadata/extractions.json',{'version':1,'method':'PDFium native text + pypdf positional layout + Windows OCR; selected human-read diagram descriptions','files':records})
    for course in sorted({r['course'] for r in records}):
        folder=ROOT/'courses'/course/'extracted';rows=[r for r in records if r['course']==course]
        lines=['# 逐页课件文本副本','', '[课程大纲](../README.md) · [原始笔记](../notes/README.md)','',
            '与原件一一对应，保留物理页码、文字层、坐标排版与必要的 OCR。`source/` 对应课程课件；`notes/` 补充先前归档在原始笔记目录的 PDF，包括批注课件。','',
            '| 原文件 | 页数 | 文本副本 |','|---|---:|---|']
        for r in rows:
            lines.append(f"| [{r['source_path']}]({rel_link(ROOT/r['source_path'],folder)}) | {r['pages']} | [{r['id']}]({rel_link(ROOT/r['extracted_path'],folder)}) |")
        (folder/'README.md').write_text('\n'.join(lines)+'\n',encoding='utf-8')
    totals=collections.Counter()
    for r in records:
        for k,v in r.items():
            if isinstance(v,int):totals[k]+=v
    print(json.dumps({'files':len(records),**dict(totals)},ensure_ascii=False))

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('operation',choices=['prepare','build'])
    args=parser.parse_args()
    prepare() if args.operation=='prepare' else build()
