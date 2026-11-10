#!/usr/bin/env python3
"""Build Jenna's portfolio using only the Python standard library."""
from pathlib import Path
import json, html, shutil, hashlib
ROOT = Path(__file__).resolve().parent
OUT = ROOT / 'dist'
DATA = json.loads((ROOT / 'content/site.json').read_text())
PROJECTS = DATA['projects']
STYLE_VERSION = hashlib.sha256((ROOT/'styles.css').read_bytes()).hexdigest()[:10]

def e(value): return html.escape(str(value), quote=True)

def image(name, alt, prefix='', cls='', eager=False):
    filename = name if Path(name).suffix else name + '.webp'
    return f'<img src="{prefix}assets/images/{e(filename)}" alt="{e(alt)}" class="{cls}" loading="{"eager" if eager else "lazy"}" decoding="async">'

def route_cover():
    return '''<div class="route-cover"><svg viewBox="0 0 600 380" aria-hidden="true"><path d="M50 350C100 290 40 180 150 150S310 220 350 100 490 30 580 70" fill="none" stroke="#d7b45b" stroke-width="1"/><path d="M80 300Q250 20 500 150" fill="none" stroke="white" stroke-width="1.5"/><g fill="#d7b45b"><circle cx="80" cy="300" r="7"/><circle cx="270" cy="145" r="7"/><circle cx="500" cy="150" r="7"/></g></svg><span>Concept development / CTIN 252</span><strong>Ibiza<br>Skylink</strong></div>'''

def card(p, i, prefix=''):
    cover=image(p['cover'],p['coverAlt'],prefix, 'contain' if p['cover'].startswith(('yellow','blue','escape','parade','ibiza')) else '') if p['cover'] else route_cover()
    status=f'<span class="status">{e(p["status"])}</span>' if p.get('status') else ''
    return f'''<a class="project-card" href="{prefix}projects/{p['slug']}.html"><div class="card-image">{cover}<span class="card-index">{i:02}</span></div><div class="card-meta"><div><h3>{e(p['title'])}</h3><p>{e(p['type'])}</p></div>{status}</div><p class="card-description">{e(p['short'])}</p></a>'''

def page(title, body, active='Home', prefix='', description='', filename='index.html'):
    nav=''.join(f'<a href="{prefix}{path}"'+(' aria-current="page"' if name==active else '')+f'>{name}</a>' for name,path in [('Home','index.html'),('About','about.html'),('Projects','projects.html'),('Ceramics','ceramics.html'),('Contact','contact.html')])
    desc=description or 'Jenna Bortnick’s creative portfolio: themed entertainment concepts, immersive environments, Blender modeling, and ceramics. University of Southern California, Class of 2029.'
    doc=f'''<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{e(title)} | Jenna Bortnick</title><meta name="description" content="{e(desc)}"><meta name="theme-color" content="#173f78"><meta property="og:title" content="{e(title)} | Jenna Bortnick"><meta property="og:description" content="{e(desc)}"><meta property="og:type" content="website"><link rel="icon" type="image/svg+xml" href="{prefix}favicon.svg"><link rel="stylesheet" href="{prefix}styles.css?v={STYLE_VERSION}"><script src="{prefix}script.js" defer></script></head><body><a class="skip" href="#main">Skip to content</a><header class="site-header container"><a class="brand" href="{prefix}index.html" aria-label="Jenna Bortnick home"><span class="brand-mark" aria-hidden="true">jb</span><span><span class="brand-name">JENNA BORTNICK</span><span class="brand-small" style="display:block">Creative portfolio</span></span></a><button class="menu-toggle" aria-expanded="false" aria-controls="main-nav">Menu <span aria-hidden="true">↗</span></button><nav class="nav" id="main-nav" aria-label="Main navigation">{nav}</nav></header><main id="main">{body}</main><footer class="site-footer container"><p>© Jenna Bortnick <span aria-hidden="true">/</span> Creative portfolio</p><div class="footer-links"><a href="{prefix}projects.html">Explore the work</a><a href="{prefix}about.html">About Jenna</a></div><p>USC • Themed Entertainment • 2029</p></footer><dialog class="lightbox" aria-label="Enlarged project image"><button class="lightbox-close" aria-label="Close image">✕</button><img alt=""><p class="lightbox-caption"></p></dialog></body></html>'''
    target=OUT/filename;target.parent.mkdir(parents=True,exist_ok=True);target.write_text(doc)

def closing(prefix=''):
    return f'<section class="closing container"><h2>A story can become a place.<br>Let’s explore what’s possible.</h2><a class="text-link" href="{prefix}contact.html">Get in touch </a></section>'

def gallery(images, prefix='', extra=''):
    figures=[]
    for name,caption in images:
        figures.append(f'<figure><button type="button" data-lightbox="{prefix}assets/images/{e(name)}.webp" data-caption="{e(caption)}" aria-label="Enlarge: {e(caption)}">{image(name,caption,prefix)}</button><figcaption>{e(caption)}</figcaption></figure>')
    return f'<div class="gallery {extra}">' + ''.join(figures) + '</div>'

def build():
    if OUT.exists(): shutil.rmtree(OUT)
    OUT.mkdir();shutil.copytree(ROOT/'assets',OUT/'assets')
    for f in ['styles.css','script.js','favicon.svg']:shutil.copyfile(ROOT/f,OUT/f)
    (OUT/'.nojekyll').touch()
    if (ROOT/'CNAME').exists(): shutil.copyfile(ROOT/'CNAME', OUT/'CNAME')
    featured=''.join(card(PROJECTS[i],i+1) for i in [4,1,2,6])
    body=f'''<div class="container"><section class="hero rise"><div class="hero-copy"><div class="eyebrow">Themed Entertainment major · Architecture minor · USC ’29</div><h1>Where imagination<br><em>takes shape.</em></h1><p>I’m Jenna, a Themed Entertainment major at the University of Southern California, pursuing a minor in Architecture. I bring a creative and analytical approach to immersive design, thinking about both the guest experience and the details that make an idea work in the real world.</p><div class="actions"><a class="button" href="projects.html">Explore my projects </a><a class="text-link" href="about.html">A little about me</a></div></div><figure class="hero-art hero-portrait">{image('jenna-portrait','Portrait of Jenna Bortnick',eager=True,cls='hero-main')}<figcaption class="image-note"><span>Jenna Bortnick</span><span>USC • Class of 2029</span></figcaption></figure></section><section class="section"><div class="section-heading"><div class="eyebrow">Selected work</div><h2>Ideas with a world<br>of their own.</h2></div><a class="text-link" href="projects.html">View all projects </a></div><div class="project-grid">{featured}</div></section></div><section class="about-band"><div class="container about-inner"><div class="about-photo">{image('jenna-portrait','Portrait of Jenna Bortnick')}</div><div class="about-text"><div class="eyebrow">The person behind the projects</div><h2>Creative thinking.<br>Practical perspective.</h2><p>I’m fascinated by how a creative idea becomes a place people can experience. I enjoy moving between sketches, spatial layouts, digital 3D models, and physical modelmaking—paying close attention to scale, details, circulation, and how everything fits together. I’m especially interested in the balance between what guests feel and what it takes to make an environment function.</p><span class="mini-label">University of Southern California • Class of 2029</span><a class="text-link" href="about.html">Meet Jenna </a></div></div></section>{closing()}'''
    page('Creative portfolio',body)
    projects=f'''<div class="container"><header class="page-head rise"><div class="eyebrow">Selected coursework & creative practice</div><h1>Projects &amp;<br><em>creative work.</em></h1><p>A collection of immersive concepts, themed environments, digital models, and creative explorations.</p><div class="filters" aria-label="Filter projects"><button class="filter" data-filter="all" aria-pressed="true">All projects <span aria-hidden="true">/ 08</span></button><button class="filter" data-filter="themed" aria-pressed="false">Themed entertainment <span aria-hidden="true">/ 06</span></button><button class="filter" data-filter="3d" aria-pressed="false">3D &amp; Blender <span aria-hidden="true">/ 02</span></button></div><p id="filter-status" class="sr-only">Showing all 8 projects.</p></header><section class="project-section" data-category="themed"><div class="project-section-head"><span>01 /</span><h2>Themed Entertainment Design</h2></div><div class="project-grid">{''.join(card(p,i+1) for i,p in enumerate(PROJECTS[:6]))}</div></section><section class="project-section" data-category="3d"><div class="project-section-head"><span>02 /</span><h2>3D Modeling &amp; Blender</h2></div><div class="project-grid">{''.join(card(p,i+7) for i,p in enumerate(PROJECTS[6:]))}</div></section><section class="ceramics-callout">{image('ceramics-1','Rapunzel-inspired ceramic tower by Jenna')}<div class="eyebrow">A different kind of making</div><h2>Working in clay.</h2><p>Sculptural forms, material exploration, and the creative possibilities of making by hand.</p><div class="actions"><a class="text-link" href="ceramics.html">Explore ceramics </a></div></div></section></div>'''
    page('Projects & creative work',projects,'Projects',filename='projects.html')
    about_resume = f'<a class="text-link" href="{e(DATA["resume"])}" target="_blank" rel="noopener noreferrer">View résumé (PDF)</a>' if DATA['resume'] else ''
    about=f'''<div class="container">
<section class="about-hero rise">
  <div>
    <div class="eyebrow">About Jenna</div>
    <h1>Hi, I’m Jenna.</h1>
    <p>I’m a Themed Entertainment major at the University of Southern California, pursuing a minor in Architecture and graduating in 2029.</p>
    <p>I’m interested in the space between imagination and reality: how creative ideas become thoughtfully designed places and experiences. My work brings together storytelling, spatial design, modelmaking, and the practical thinking that helps an idea work in the real world.</p>
    <div class="bio-details">
      <div><h2>Education</h2><p>University of Southern California<br>Themed Entertainment<br>Architecture minor<br>Class of 2029</p></div>
      <div><h2>Creative practice</h2><p>Concept development<br>Spatial storytelling<br>Digital and physical modeling</p></div>
    </div>
    <div class="actions"><a class="text-link" href="assets/jenna-bortnick-resume.pdf" target="_blank" rel="noopener noreferrer">View résumé (PDF)</a><a class="button" href="projects.html">Explore my projects </a></div>
  </div>
  <figure><img src="assets/images/jenna-portrait.webp" alt="Portrait of Jenna" class="portrait" loading="eager" decoding="async"><figcaption>Creative ideas, brought into the real world.</figcaption></figure>
</section>
<section class="process">
  <div class="eyebrow">How I think & create</div>
  <h2>Imagination, with a plan.</h2>
  <p>I approach design with both a creative and analytical mindset. I like starting with rough sketches, then developing ideas through detailed layouts and 3D models. I’m drawn to the details that make a space feel convincing, from scale, proportions, and sightlines to textures, circulation, and how everything fits together.</p>
  <p>I always think about the experience from more than one perspective: what guests notice and how they move through a space, as well as how that space can be built, operated, and brought to life. I want people to feel like they are a character in the world they have stepped into.</p>
</section>
<section class="experience">
  <img src="assets/images/disney-portrait-original.jpeg" alt="Jenna during her Disney College Program attractions role" loading="lazy" decoding="async">
  <div>
    <div class="eyebrow">Experience that shaped my perspective</div>
    <h2>Disney College Program</h2>
    <p><strong>Attractions Cast Member · Walt Disney World</strong></p>
    <p>During a three-month summer internship with the Disney College Program, I worked in attractions at The Twilight Zone Tower of Terror and as an amphitheater attendant for Fantasmic! At Tower of Terror, I welcomed guests, answered questions, helped nervous visitors feel comfortable, checked safety restraints, dispatched the attraction, and monitored operations from the control desk.</p>
    <p>The experience gave me a guest-facing and operational perspective on immersive entertainment. I loved seeing the excitement of first-time visitors, learning how the attraction worked behind the scenes, and noticing how the atmosphere and the people working in a space all contribute to the experience.</p>
  </div>
</section>
<div class="container">
  <div class="gallery" aria-label="Disney College Program photos">
    <figure><img src="assets/images/disney-team.webp" alt="Jenna with her Disney College Program team" loading="lazy" decoding="async"><figcaption>The people behind the experience.</figcaption></figure>
  </div>
</div>
<section class="process">
  <div class="eyebrow">Beyond the blueprint</div>
  <h2>Stories beyond the studio.</h2>
  <p>Outside of my academic and creative work, I’m an avid fan of movies, television, video games, and books. I love getting lost in imaginative stories and exploring the worlds built around them.</p>
</section>
<section class="process">
  <div class="eyebrow">What I’m working toward</div>
  <h2>From the first idea to the finished experience.</h2>
  <p>I’m interested in opportunities that bring creative vision and practical execution together, especially themed entertainment, immersive environments, modelmaking, and project management. I enjoy developing digital and physical models, thinking through how a design can function, and coordinating the details that help a larger project come together.</p>
  <p>My goal is to help create places that capture people’s imaginations, invite exploration, and make them feel part of another world—while making sure the idea can work beyond the page or screen.</p>
</section>
</div>'''
    page('About',about,'About',filename='about.html')
    ceramic_work=json.loads((ROOT/'content/ceramics.json').read_text())
    ceramic_sections=''.join(f'<section class="process"><div class="eyebrow">Ceramics</div><h2>{e(work["title"])}</h2><p>{e(work["description"])}</p>{gallery(work["images"],extra="ceramic-gallery")}</section>' for work in ceramic_work)
    ceramics=f'''<div class="container"><header class="page-head rise"><div class="eyebrow">Fine art & material exploration</div><h1>Made by hand.<br><em>Shaped in clay.</em></h1><p>Story-inspired sculptures, expressive characters, and functional pieces with a little imagination.</p></header>{ceramic_sections}</div>'''
    page('Ceramics',ceramics,'Ceramics',filename='ceramics.html')
    links=''
    if DATA['email']:links+=f'<a class="contact-item" href="mailto:{e(DATA["email"])}"><small>Email</small><span class="contact-action">Email Jenna</span><span class="contact-detail">{e(DATA["email"])}</span></a>'
    if DATA['linkedin']:links+=f'<a class="contact-item" href="{e(DATA["linkedin"])}" target="_blank" rel="noopener noreferrer"><small>LinkedIn</small><span class="contact-action">Open LinkedIn profile</span></a>'
    if DATA['resume']:links+=f'<a class="contact-item" href="{e(DATA["resume"])}" target="_blank" rel="noopener noreferrer"><small>Résumé</small><span class="contact-action">View résumé (PDF)</span></a>'
    if not links:links='<p>Contact details will be added soon.</p><p class="contact-note">In the meantime, take a look around the portfolio to explore my work and creative interests.</p><div class="actions"><a class="text-link" href="projects.html">Explore my projects </a></div>'
    contact=f'''<div class="container"><section class="contact-layout rise"><div><div class="eyebrow">Contact</div><h1>Let’s make<br>something<br><em>memorable.</em></h1><p>Have a project, an opportunity, or a shared interest in themed entertainment? This is where we can connect.</p></div><div class="contact-panel"><h2>Start a conversation.</h2>{links}<span class="mini-label">Jenna Bortnick / USC • Themed Entertainment</span></div></section></div>'''
    page('Contact',contact,'Contact',filename='contact.html')
    for i,p in enumerate(PROJECTS):
        prefix='../';nxt=PROJECTS[(i+1)%len(PROJECTS)]
        cover=image(p['cover'],p['coverAlt'],prefix,eager=True) if p['cover'] else route_cover()
        sub=f'<p class="subtitle">{e(p["subtitle"])}</p>' if p.get('subtitle') else ''
        sections=''.join(f'<section class="process"><div class="eyebrow">Design & development</div><h2>{e(s["title"])}</h2><p>{e(s["text"])}</p>{gallery(s["images"],prefix)}</section>' for s in p['sections'])
        notes='Selected presentation pages are shown in their original context. Collaborative work and reference imagery are identified in the project credits and captions.' if p['slug'] in ['as-the-trees-grow','yellow-submarine','ibiza-skylink','blue-horizon','traveling-escape-room'] else 'A selection of supplied project imagery and process studies.'
        body=f'''<div class="container"><nav class="crumb" aria-label="Breadcrumb"><a href="../projects.html">Projects</a><span aria-hidden="true">/</span><span>{e(p['title'])}</span></nav><header class="detail-head rise"><div><div class="eyebrow">{i+1:02} / {e(p['type'])}</div><h1>{e(p['title'])}</h1>{sub}</div><p class="short">{e(p['short'])}</p></header><div class="detail-cover">{cover}</div><section class="detail-overview"><div><h2>The project</h2><p>{e(p['overview'])}</p></div><dl class="details-list"><div><dt>Context</dt><dd>{e(p['course'])}</dd></div><div><dt>Creative focus</dt><dd>{'<br>'.join(e(x) for x in p['focus'])}</dd></div></dl></section>{sections}<p class="source-note">{e(notes)}</p>{closing(prefix)}</div>'''
        page(p['title'],body,'Projects',prefix,p['overview'],f'projects/{p["slug"]}.html')
    page('Page not found','<section class="container error-page"><div class="eyebrow">404 / A little off the map</div><h1>Let’s find your way back.</h1><p>This page isn’t here. There are plenty of worlds to explore in the portfolio.</p><div class="actions"><a class="button" href="index.html">Back to home</a></div></section>',filename='404.html')
    print(f'Built {len(list(OUT.rglob("*.html")))} pages in {OUT}')

if __name__=='__main__':build()
