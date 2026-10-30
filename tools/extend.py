"""Laos: add the Lao Official Gazette's list of all current laws (public sheet linked from laoofficialgazette.gov.la) to the catalogue act."""
import csv, json, re, sys, hashlib
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / 'world-law'))
from cat_lib import merge_entries
raw = (HERE / '.tmp/sheet.csv').read_bytes()
rows = list(csv.reader(raw.decode('utf8').splitlines()))
data = [r for r in rows[7:] if len(r) > 7 and r[1].strip()]
def iso(s):
    m = re.fullmatch(r'\s*(\d{1,2})/(\d{1,2})/(\d{4})\s*', s or '')
    return f'{int(m.group(3)):04d}-{int(m.group(2)):02d}-{int(m.group(1)):02d}' if m else None
entries, bad, used = [], [], set()
for r in data:
    title, status, year, agency, num, d1, d2 = [x.strip() for x in r[1:8]]
    date, gaz = iso(d1), iso(d2)
    if not date:
        bad.append(r[:8]); continue
    num = num or 'not given'
    key = f"law-{date}-{num.lower()}"
    key = re.sub(r'[^a-z0-9]+', '-', key).strip('-')
    k, i = key, 1
    while k in used: i += 1; k = f'{key}-{i}'
    used.add(k)
    lines = [f'# {title}', f'Number: {num}', f'Date of the law: {date}']
    if gaz: lines.append(f'Published in the Lao Official Gazette: {gaz}')
    lines += [f'Responsible body: {agency}', f'Gazette citation: Lao Official Gazette (ຈົດໝາຍເຫດທາງລັດຖະການ)' + (f', published {gaz}' if gaz else ''),
              'Record: https://laoofficialgazette.gov.la/']
    entries.append((date, k, f'No. {num}: ' + title[:70], '\n'.join(lines) + '\n'))
if not any(a['slug'] == 'catalogue' for a in json.load(open(HERE / 'corpus.json', encoding='utf8'))['acts']):
    pass
c = json.load(open(HERE / 'corpus.json', encoding='utf8'))
if not any(a['slug'] == 'catalogue-gazette' for a in c['acts']):
    c['acts'].append({'slug': 'catalogue-gazette', 'short': 'Gazette', 'title': 'Catalogue of the current laws of Laos listed by the Lao Official Gazette (title, number, date, gazette date; no law text)',
                      'url': 'https://laoofficialgazette.gov.la/', 'first_law': None, 'earlier_laws': [], 'versions': []})
merge_entries(c, 'catalogue-gazette', entries, 'catalogue-gazette', "Catalogue entries dated by the date of the law as listed by the Lao Official Gazette; facts only, no law text.",
              'https://laoofficialgazette.gov.la/', hashlib.sha256(raw).hexdigest(), 'https://laoofficialgazette.gov.la/')
a = [a for a in c['acts'] if a['slug'] == 'catalogue-gazette'][0]
a['first_law'] = None
c['sources'] = [s for s in c['sources'] if s['name'] != 'Lao Official Gazette, list of all laws'] + [{'name': 'Lao Official Gazette, list of all laws', 'url': 'https://laoofficialgazette.gov.la/', 'retrieved': '2026-10-30',
    'licence': 'Facts only (title, number, dates, responsible body); no law text copied. The sheet is the "all laws" list the Gazette home page links to.', 'notes': 'Public Google Sheet exported as CSV; Lao titles copied as the list gives them.'}]
c['decisions'] = [d for d in c['decisions'] if not d.startswith('Lao Official Gazette list')]
c['decisions'].append(f'Lao Official Gazette list of all laws: {len(entries)} laws (the 2025 Constitution, laws and amending laws) with number, date of the law and Gazette publication date, dated by the date of the law. {len(bad)} rows without a parsable date or number were left out. Lao titles are copied as listed. No law text and no OCR.')
json.dump(c, open(HERE / 'corpus.json', 'w', encoding='utf8', newline='\n'), ensure_ascii=False, indent=1)
print(len(entries), 'entries; bad', bad)
