"""Check generated HTML, local links, media, and responsive essentials."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit,unquote
import sys
root=Path(__file__).resolve().parents[1]/'dist';errors=[];pages=list(root.rglob('*.html'));refs=0
class Check(HTMLParser):
 def __init__(self,path):super().__init__();self.path=path;self.h1=0;self.title=False;self.viewport=False;self.dialog_image=False
 def handle_starttag(self,tag,attrs):
  global refs
  a=dict(attrs)
  if tag=='h1':self.h1+=1
  if tag=='title':self.title=True
  if tag=='meta' and a.get('name')=='viewport':self.viewport=True
  if tag=='img' and 'alt' not in a:errors.append(f'{self.path}: image missing alt')
  for attr in ['href','src','poster']:
   value=a.get(attr,'')
   if not value or value.startswith(('#','mailto:','https:','http:','data:')):continue
   refs+=1;p=unquote(urlsplit(value).path)
   target=(self.path.parent/p).resolve()
   if not target.is_relative_to(root.resolve()):errors.append(f'{self.path}: link escapes site {value}')
   elif not target.exists():errors.append(f'{self.path}: missing {value}')
for p in pages:
 parser=Check(p);parser.feed(p.read_text())
 if parser.h1!=1:errors.append(f'{p}: expected 1 h1, found {parser.h1}')
 if not parser.title or not parser.viewport:errors.append(f'{p}: missing title/viewport')
for p in (root/'assets').rglob('*'):
 if p.is_file() and p.stat().st_size>=100*1024*1024:errors.append(f'{p}: exceeds GitHub file limit')
if errors:print('\n'.join(errors));sys.exit(1)
print(f'PASS: {len(pages)} pages, {refs} local links/assets; all files resolve. Every page has one h1, a title, and a viewport.')
