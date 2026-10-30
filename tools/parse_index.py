"""Laos: parse .tmp/pages/*.html (Official Gazette index) into .tmp/docs.json."""
import re, html, json, glob
rows = []
for f in sorted(glob.glob('.tmp/pages/p*.html')):
    s = open(f, encoding='utf8', errors='ignore').read()
    for r in re.findall(r'<tr[^>]*>(.*?)</tr>', s, re.S):
        tds = re.findall(r'<td[^>]*>(.*?)</td>', r, re.S)
        if len(tds) < 8: continue
        txt = [re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]+>', '', t))).strip() for t in tds]
        m = re.search(r'id=(\d+)', tds[5]); en = re.search(r'href="([^"]+\.pdf)"', tds[6]); lo = re.search(r'href="([^"]+\.pdf)"', tds[7])
        d1 = re.fullmatch(r'(\d\d)-(\d\d)-(\d{4})', txt[2]); d2 = re.fullmatch(r'(\d\d)-(\d\d)-(\d{4})', txt[3])
        if not m or not d1: continue
        rows.append({'id': int(m.group(1)), 'title': txt[0], 'agency': txt[1], 'issued': '-'.join(d1.groups()[::-1]),
                     'gazette': '-'.join(d2.groups()[::-1]) if d2 else None, 'type': txt[4],
                     'en_pdf': en.group(1) if en else None, 'lo_pdf': lo.group(1) if lo else None, 'page': f[-8:-5]})
seen = {}
for r in rows: seen.setdefault(r['id'], r)
rows = sorted(seen.values(), key=lambda r: (r['issued'], r['id']))
json.dump(rows, open('.tmp/docs.json', 'w', encoding='utf8'), ensure_ascii=False, indent=0)
print(len(rows))
