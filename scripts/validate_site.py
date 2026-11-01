"""Offline verification of the generated public site and its publication boundary."""
from pathlib import Path
from urllib.parse import urlsplit,unquote
import json,re,sys
from bs4 import BeautifulSoup
ROOT=Path(__file__).resolve().parents[1]
SITE=ROOT/'site'
release=json.loads((ROOT/'release.json').read_text())
errors=[]; links=0; downloads=0; pages=list(SITE.rglob('*.html'))
ids={}
for p in pages:
    soup=BeautifulSoup(p.read_text(),'html.parser')
    ids[p.resolve()]={n.get('id') for n in soup.select('[id]')}
for p in pages:
    html=p.read_text(); soup=BeautifulSoup(html,'html.parser')
    for a in soup.select('a[href]'):
        href=a['href']; u=urlsplit(href)
        if '/releases/' in u.path and u.netloc=='github.com':
            downloads+=1
            if a.get('target')!='_blank' or not {'noopener','noreferrer'}.issubset(set(a.get('rel',[]))): errors.append(f'{p.relative_to(SITE)} unsafe release/download anchor {href}')
            allowed={release['release_url'],*(x['url'] for x in release['assets'].values())}
            if href not in allowed: errors.append('Unverified release URL: '+href)
        if u.scheme or u.netloc: continue
        if not u.path: target=p
        elif u.path.startswith('/'): target=SITE/unquote(u.path.lstrip('/'))
        else: target=p.parent/unquote(u.path)
        if target.is_dir(): target=target/'index.html'
        target=target.resolve();links+=1
        if not target.exists(): errors.append(f'{p.relative_to(SITE)} missing link {href}')
        elif u.fragment and target.suffix=='.html' and unquote(u.fragment) not in ids.get(target,set()): errors.append(f'{p.relative_to(SITE)} missing anchor {href}')
    for node in soup.select('img[src],script[src],link[rel=stylesheet]'):
        src=node.get('src',node.get('href',''));u=urlsplit(src)
        if u.scheme or u.netloc:
            errors.append(f'Unexpected externally fetched active asset: {src}')
        elif not ((SITE/unquote(u.path.lstrip('/'))) if u.path.startswith('/') else (p.parent/unquote(u.path))).resolve().exists():errors.append(f'Missing asset: {src}')
    if '{{ ' in html or '<!-- fields:' in html or '<!-- tax-fields:' in html: errors.append(f'Unresolved marker: {p}')
    if '/Users/src/' in html or '/Users/kiranparmar/' in html: errors.append(f'Private absolute path: {p}')
# Repository may contain only documentation/build tooling; never installer/app/data payloads.
for p in ROOT.rglob('*'):
    if not p.is_file() or '.git' in p.relative_to(ROOT).parts or 'site' in p.relative_to(ROOT).parts or '__pycache__' in p.parts: continue
    if p.suffix.lower() in {'.dmg','.exe','.db','.sqlite','.csv','.zip','.pdf'} or p.name in {'app.py','schema.sql','.ledgerly-secret'}: errors.append(f'Forbidden public-repo payload: {p.relative_to(ROOT)}')
assert (SITE/'CNAME').read_text().strip()=='ledgerly-app.com'
assert (ROOT/'CNAME').read_text().strip()=='ledgerly-app.com'
search=json.loads((SITE/'search/search_index.json').read_text())
text=' '.join(str(x) for x in search['docs'])
for phrase in ('Funded','Tracking','Reconciliation','Password','Inheritance','headroom'): 
    if phrase.lower() not in text.lower(): errors.append('Search missing: '+phrase)
assert len(pages)>=40
if errors:
    print('\n'.join(errors));sys.exit(1)
print(f'PASS: {len(pages)} HTML pages; {links} internal links/anchors; {downloads} safe verified release/download anchors; search index, self-hosted assets, CNAME and publication boundary.')
