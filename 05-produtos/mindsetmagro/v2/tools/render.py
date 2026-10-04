"""Generate the book, workbook and offline reference from identical structured blocks.
Run: python tools/render.py --output /absolute/output (requires all 30 days).
No live app, commercial entitlement, external AI or server is simulated here.
"""
from pathlib import Path
import argparse,json,hashlib,html,copy,xml.etree.ElementTree as ET
from reportlab.platypus import SimpleDocTemplate,Paragraph,Spacer,PageBreak,KeepTogether,Flowable,Image
from reportlab.lib.styles import getSampleStyleSheet,ParagraphStyle
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.enums import TA_CENTER
from reportlab.platypus.tableofcontents import TableOfContents
class BookDoc(SimpleDocTemplate):
 def afterFlowable(self,flowable):
  if isinstance(flowable,Paragraph) and flowable.style.name=="H1X" and flowable.getPlainText()!="Mapa de leitura":
   self.notify("TOCEntry",(0,flowable.getPlainText(),self.page))
from svglib.svglib import svg2rlg
ROOT=Path(__file__).resolve().parents[1]
class Lines(Flowable):
 def __init__(self,h=85): Flowable.__init__(self);self.width=390;self.height=h
 def draw(self):
  self.canv.setStrokeColor(colors.HexColor('#c7d1ca'));self.canv.setLineWidth(.5)
  for y in range(8,int(self.height),19): self.canv.line(0,y,self.width,y)
def load():
 days=sorted([json.loads(p.read_text()) for p in (ROOT/'days').glob('*.json')],key=lambda d:d['day'])
 if [d['day'] for d in days]!=list(range(1,31)): raise SystemExit('Refusing final render: need days 1–30 exactly once.')
 sections=[]
 for name in ['prebook']:
  p=ROOT/(name+'.json')
  if not p.exists(): raise SystemExit('Missing '+str(p))
  obj=json.loads(p.read_text());sections+=obj if isinstance(obj,list) else [obj]
 sections+=days
 p=ROOT/'postbook.json'
 if not p.exists():raise SystemExit('Missing postbook.json')
 obj=json.loads(p.read_text());sections+=obj if isinstance(obj,list) else [obj]
 claims_path=ROOT/'research/claims-evidence.json'
 if claims_path.exists():
  claims=json.loads(claims_path.read_text()).get('claims',[])
  refs=[{'id':'ref-'+c['claim_id'],'type':'reading','title':c['claim_id']+' · '+c.get('mechanism',''),'content':[c.get('bibliographic_reference') or ((c.get('authors') or '')+' ('+str(c.get('year',''))+'). '+c.get('source_title','')+'. '+c.get('url',''))],'fields':[]} for c in claims]
  sections.append({'id':'references','title':'Referências e rastreabilidade','blocks':refs})
 fields=[f for d in sections for b in d.get('blocks',[]) for f in b.get('fields',[])]
 ids=[f['id'] for f in fields]
 if len(set(ids))!=len(ids):raise SystemExit('Duplicate field IDs')
 return sections,days,fields

def styles():
 for name,path in [('Body','DejaVuSans.ttf'),('Bold','DejaVuSans-Bold.ttf'),('Serif','DejaVuSerif.ttf')]:pdfmetrics.registerFont(TTFont(name,'/usr/share/fonts/truetype/dejavu/'+path))
 s=getSampleStyleSheet()
 for key in ['Normal','BodyText']:s[key].fontName='Body';s[key].fontSize=10;s[key].leading=15;s[key].spaceAfter=8;s[key].textColor=colors.HexColor('#293b35')
 s.add(ParagraphStyle('TitleX',fontName='Serif',fontSize=29,leading=37,textColor=colors.HexColor('#24483f'),spaceAfter=18))
 s.add(ParagraphStyle('AuthorX',fontName='Serif',fontSize=20,leading=26,textColor=colors.HexColor('#24483f')))
 s.add(ParagraphStyle('H1X',fontName='Serif',fontSize=22,leading=29,textColor=colors.HexColor('#24483f'),spaceAfter=15))
 s.add(ParagraphStyle('H2X',fontName='Bold',fontSize=12,leading=17,textColor=colors.HexColor('#24483f'),spaceBefore=13,spaceAfter=7,keepWithNext=True))
 s.add(ParagraphStyle('MetaX',fontName='Body',fontSize=8,leading=12,textColor=colors.HexColor('#62766c'),spaceAfter=8))
 return s

def textparts(b):
 c=b.get('content',[])
 return c if isinstance(c,list) else [str(c)]
def esc(t):return html.escape(str(t)).replace('\n','<br/>')
def pdf_render(sections,out,workbook=False):
 if workbook:sections=[d for d in sections if any(b.get('fields') or b.get('type') in ['mission','if_then','ritual','health_note','fruit_review','installation'] for b in d.get('blocks',[]))]
 s=styles(); story=[];title='Caderno Vivo' if workbook else 'MINDSETmagro™ 2.0'
 story+=[Spacer(1,95),Paragraph('RELACIONE-SE®',s['MetaX']),Paragraph(title,s['TitleX']),Paragraph('Uma travessia de 30 dias para aliviar excessos, recuperar autoria e cuidar das próprias escolhas.',s['BodyText']),Spacer(1,38),Paragraph('Sol Lima',s['AuthorX']),Spacer(1,120),Paragraph('Edição de revisão · 2.0.0-review.1',s['MetaX']),PageBreak()]
 story+=[Paragraph('Mapa de leitura',s['H1X'])]
 toc=TableOfContents();toc.levelStyles=[ParagraphStyle('TOC',fontName='Body',fontSize=10,leading=16,spaceBefore=5)];story.append(toc)
 story.append(PageBreak())
 for i,d in enumerate(sections):
  if i:story.append(PageBreak())
  if d.get('day') in [1,6,11,16,21,26]:
   idx=(d['day']-1)//5
   goals=[x['objective'] for x in json.loads((ROOT/'traversals.json').read_text())]
   story.extend([Spacer(1,95),Paragraph('TRAVESSIA '+['I','II','III','IV','V','VI'][idx],s['MetaX']),Paragraph(esc(d['traversal']),s['H1X']),Paragraph('Dias '+str(d['day'])+' a '+str(d['day']+4),s['MetaX']),Spacer(1,25),Paragraph(goals[idx],s['BodyText']),PageBreak()])
  if d.get('traversal'):story.append(Paragraph(esc(d['traversal']),s['MetaX']))
  label=(f"Dia {d['day']:02} · " if d.get('day') else '')+d['title']
  story.append(Paragraph(esc(label),s['H1X']))
  if d.get('objective'):story.append(Paragraph(esc(d['objective']),s['BodyText']))
  if workbook:story.append(Paragraph('Registre apenas o necessário. Você pode deixar campos opcionais em branco. Corpo e alimentação são escolhas de participação.',s['MetaX']))
  for b in d.get('blocks',[]):
   fs=b.get('fields',[])
   if workbook and not fs and b.get('type') not in ['mission','if_then','ritual','health_note','fruit_review','installation']:continue
   if b.get('title'):story.append(Paragraph(esc(b['title']),s['H2X']))
   for t in textparts(b):story.append(Paragraph(esc(t),s['BodyText']))
   vr=b.get('visual_ref')
   if vr:
    visuals=json.loads((ROOT/'visual-assets.json').read_text())
    match=next((v for v in visuals if v['id']==vr),None)
    vp=ROOT/match['path'] if match and match.get('path') else ROOT/'assets'/(str(vr).replace('assets/','').removesuffix('.svg')+'.svg')
    if vp.exists():
     drawing=svg2rlg(str(vp)); ratio=390/drawing.width;drawing.width*=ratio;drawing.height*=ratio;drawing.scale(ratio,ratio);story.append(drawing)
   for f in fs:
    opt=' · opcional: '+str(f['opt_in']) if f.get('opt_in') else ''
    story.append(Paragraph(esc(f['label']+opt),s['H2X']))
    if f.get('options'):story.append(Paragraph(esc(' / '.join(str(x) for x in f['options'])),s['MetaX']))
    if workbook:story.append(Lines(95 if f.get('kind')=='textarea' else 45))
    else:story.append(Paragraph('Registre no seu Caderno Vivo.',s['MetaX']))
 def page(c,doc):
  if doc.page==1:
   c.setFillColor(colors.HexColor('#24483f'));c.rect(0,0,18,720,fill=1,stroke=0)
   c.setStrokeColor(colors.HexColor('#91aa8f'));c.setLineWidth(1.4)
   c.line(405,130,405,280);c.bezier(405,225,350,270,360,300,405,255);c.bezier(405,250,458,280,466,310,405,282)
   c.line(405,130,365,95);c.line(405,130,450,90);c.line(405,130,405,75)
   return
  c.setStrokeColor(colors.HexColor('#d5ded5'));c.line(45,39,465,39);c.setFont('Body',7);c.setFillColor(colors.HexColor('#63766d'));c.drawString(45,25,'MINDSETmagro 2.0 · Sol Lima · edição de revisão');c.drawRightString(465,25,str(doc.page))
 doc=BookDoc(str(out),pagesize=(510,720),rightMargin=60,leftMargin=60,topMargin=52,bottomMargin=58,title=title,author='Sol Lima')
 doc.multiBuild(story,onFirstPage=page,onLaterPages=page)

def main():
 a=argparse.ArgumentParser();a.add_argument('--output',required=True);args=a.parse_args();out=Path(args.output);out.mkdir(parents=True,exist_ok=True)
 sections,days,fields=load();source=json.dumps(sections,ensure_ascii=False,sort_keys=True);sha=hashlib.sha256(source.encode()).hexdigest()
 (out/'mindsetmagro-fonte-renderizada.json').write_text(json.dumps({'source_hash':sha,'sections':sections},ensure_ascii=False,indent=2))
 pdf_render(sections,out/'MINDSETmagro-2.0-Livro.pdf');pdf_render(sections,out/'MINDSETmagro-2.0-Caderno-Vivo.pdf',True)
 template=(ROOT/'tools/reference.html').read_text()
 vtexts={}
 for ap in (ROOT/'assets').glob('*.svg'):
  groups=[]
  for tx in ET.fromstring(ap.read_text()).iter('{http://www.w3.org/2000/svg}text'):
   text=''.join(tx.itertext())
   if tx.attrib.get('font-size')=='22':groups.append(text)
   elif tx.attrib.get('font-size')=='19' and groups:groups[-1]+=' '+text
   elif tx.attrib.get('font-size') not in ['26']:groups.append(text)
  vtexts[ap.stem]=groups
 for v in json.loads((ROOT/'visual-assets.json').read_text()):
  if v.get('path'):vtexts[v['id']]=vtexts.get(Path(v['path']).stem,[])
 payload=json.dumps({'sections':sections,'source_hash':sha,'visual_text':vtexts},ensure_ascii=False).replace('<','\\u003c')
 assets={p.stem:p.read_text() for p in (ROOT/'assets').glob('*.svg')}
 for v in json.loads((ROOT/'visual-assets.json').read_text()):
  if v.get('path') and (ROOT/v['path']).exists():assets[v['id']]=(ROOT/v['path']).read_text()
 template=template.replace('/*__DATA__*/',payload).replace('/*__ASSETS__*/',json.dumps(assets,ensure_ascii=False).replace('<','\\u003c'))
 (out/'MINDSETmagro-2.0-Interativo.html').write_text(template)
 lock_path=ROOT/'source-lock.json'
 canonical_lock_hash=hashlib.sha256(lock_path.read_bytes()).hexdigest() if lock_path.exists() else None
 report={'canonical_source_lock_hash':canonical_lock_hash,'canonical_source_lock_hash_definition':'SHA256 of source-lock.json bytes at render time','source_hash':sha,'days':len(days),'fields':len(fields),'blocks':sum(len(d.get('blocks',[])) for d in sections),'outputs':['MINDSETmagro-2.0-Livro.pdf','MINDSETmagro-2.0-Caderno-Vivo.pdf','MINDSETmagro-2.0-Interativo.html'],'source':'same sections and field IDs for all renderers','limitations':['Offline gate is editable and not commercial security','Local data needs export backup; no cloud sync','No AI endpoint in standalone reference','Visual review and browser verification required']}
 (out/'render-report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2));print(json.dumps(report,ensure_ascii=False))
if __name__=='__main__':main()
