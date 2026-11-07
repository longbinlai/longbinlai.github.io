"""Build the native HTML/CSS site from the retained Markdown content."""
from pathlib import Path
import argparse
import datetime
import html
import json
import re
import shutil
import xml.etree.ElementTree as ET
from urllib.parse import urlsplit
import markdown
import yaml
from translations import chinese, TEXT

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'dist'
BASE = 'https://longbinlai.github.io'
E = lambda value: html.escape(str(value or ''), quote=True)
MD = markdown.Markdown(extensions=['extra', 'sane_lists'])

def render(text):
    # Convert old Academic figure shortcodes while preserving bundled image paths.
    text = re.sub(r'\{\{[<%]\s*figure\s+([^}]+)[>%]\}\}', lambda m: '![](' + (re.search(r'src="([^"]+)"', m[1])[1] if re.search(r'src="([^"]+)"', m[1]) else '') + ')', text)
    text = re.sub(r'\{\{[<%].*?[>%]\}\}', '', text)
    return MD.reset().convert(text)

def read(path):
    text = path.read_text()
    _, front, body = text.split('---', 2)
    data = yaml.safe_load(front)
    english = path.with_name('index.en.md')
    if path.name == 'index.md' and english.exists():
        _, translated_front, body = english.read_text().split('---', 2)
        data.update(yaml.safe_load(translated_front))
    data.update(body=body.strip(), source=path, route='/' + str(path.parent.relative_to(ROOT / 'content')) + '/')
    return data

def records(kind):
    return sorted([d for p in (ROOT/'content'/kind).rglob('index.md') if not (d := read(p)).get('draft') and not (kind == 'talk' and p.parent.name == 'example')], key=lambda d: str(d.get('date', '')), reverse=True)

def local_url(value, d):
    if not value: return ''
    value = str(value)
    if urlsplit(value).scheme or value.startswith(('/', '#')): return value
    return '/' + value if value.startswith('files/') else d['route'] + value

def resources(d):
    links = []
    for key, label in [('url_course','Open course'),('url_pdf','PDF'),('url_code','Code'),('url_docs','Docs'),('url_slides','Slides'),('url_video','Video'),('url_blog','Blog')]:
        if d.get(key): links.append(f'<a href="{E(local_url(d[key],d))}">{label} ↗</a>')
    if (d['source'].parent/'cite.bib').exists(): links.append(f'<a href="{E(d["route"])}cite.bib">BibTeX</a>')
    if d.get('doi'):
        doi = re.sub(r'^https?://doi.org/', '', str(d['doi']))
        links.append(f'<a href="https://doi.org/{E(doi)}">DOI ↗</a>')
    return '<div class="resources">' + ''.join(links) + '</div>'

def page(title, body, route='/', description='Longbin (Robin) Lai — graph databases, query optimization, distributed systems, and AI.'):
    return f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{E(title)} · Longbin (Robin) Lai</title><meta name="description" content="{E(description)}"><meta name="theme-color" content="#faf9f6"><link rel="canonical" href="{BASE}{route}"><meta property="og:title" content="{E(title)} · Longbin (Robin) Lai"><meta property="og:description" content="{E(description)}"><meta property="og:type" content="website"><meta property="og:url" content="{BASE}{route}"><link rel="icon" href="/favicon.ico"><script src="/assets/theme.js"></script><link rel="stylesheet" href="/assets/site.css"><script src="/assets/site.js" defer></script><script src="/assets/language.js" defer></script></head><body>
<a class="skip" href="#main">Skip to content</a><header class="header"><div class="wrap nav"><a class="brand" href="/" aria-label="Longbin Lai home">Longbin (Robin) Lai<span>.</span></a><nav aria-label="Main navigation"><a href="/#work">Work</a><a href="/publication/">Research</a><a href="/talk/">Talks</a><a href="/post/">Writing</a><a href="/#about">About</a></nav><a href="/zh{route}" class="language-toggle" aria-label="切换到中文" lang="zh-CN">中文</a><button id="theme-toggle" class="theme-toggle" type="button" aria-label="Switch to dark mode" aria-pressed="false"><svg class="moon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" aria-hidden="true"><path d="M20.5 14A8.5 8.5 0 0 1 10 3.5 8.5 8.5 0 1 0 20.5 14Z"/></svg><svg class="sun" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" aria-hidden="true"><circle cx="12" cy="12" r="4"/><path d="M12 2v2m0 16v2M2 12h2m16 0h2M5 5l1.5 1.5m11 11L19 19M5 19l1.5-1.5m11-11L19 5"/></svg></button></div></header>
<main id="main" class="wrap">{body}</main><footer><div class="wrap"><span>© {datetime.date.today().year} Longbin (Robin) Lai</span><span>Graphs, systems, and the ideas between them. <a href="https://github.com/longbinlai">GitHub ↗</a></span></div></footer></body></html>'''

ROUTES=[]
def write(route, title, body):
    dest=OUT/route.strip('/')/'index.html'
    dest.parent.mkdir(parents=True,exist_ok=True)
    if route in ['/publication/', '/post/', '/project/', '/talk/']:
        body = body.replace('<h2>', '<h1>', 1).replace('</h2>', '</h1>', 1)
    zh_body = body
    if route.startswith('/post/') and route != '/post/':
        source = ROOT/'content'/route.strip('/')/'index.md'
        translation = source.with_name('index.zh.md')
        if translation.exists():
            original = read(source)
            translated = read(translation)
            zh_body = body.replace(render(original['body']), render(translated['body']))
    document = page(title,body,route)
    dest.write_text(document)
    zh_dest = OUT/'zh'/route.strip('/')/'index.html'
    zh_dest.parent.mkdir(parents=True,exist_ok=True)
    biography = render(read(ROOT/'content/authors/admin/_index.md')['body']) if route == '/' else ''
    zh_dest.write_text(chinese(page(title,zh_body,route),route,biography))
    ROUTES.append('/zh' + route)
    ROUTES.append(route)

def paper(d):
    year=str(d.get('date',''))[:4]
    authors=', '.join(('Longbin Lai' if a == 'admin' else str(a) for a in d.get('authors',[])))
    authors=E(authors).replace('Longbin Lai','<strong>Longbin Lai</strong>')
    return f'''<article class="paper" data-paper data-year="{year}"><span class="paper-year">{year}</span><div><h3><a href="{d['route']}">{E(d['title'])}</a></h3><p class="authors">{authors}</p><div class="venue">{render(str(d.get('publication','')))}</div>{resources(d)}</div></article>'''

def section_head(kicker,title,link='',label='View all'):
    return f'<div class="section-head"><div><p class="eyebrow">{kicker}</p><h2>{title}</h2></div>'+ (f'<a class="text-link" href="{link}">{label} ↗</a>' if link else '')+'</div>'

def talk_metadata(d):
    items=[]
    if d.get('date'):
        date = str(d['date'])[:10]
        items.append(f'<div><dt>Date</dt><dd><time datetime="{E(date)}">{E(date)}</time></dd></div>')
    if d.get('location'):
        items.append(f'<div><dt>Location</dt><dd>{E(d["location"])}</dd></div>')
    return '<dl class="talk-meta">' + ''.join(items) + '</dl>' if items else ''

def contact_section():
    config = json.loads((ROOT/'content/social.json').read_text())
    x_icon = '<svg viewBox="0 0 24 24" aria-hidden="true" fill="currentColor"><path d="M18.9 2H22l-6.8 7.8L23.2 22h-6.3L12 14.6 5.5 22H2.3l7.9-9L.8 2h6.4l4.5 6.8L18.9 2ZM17.8 20h1.7L6.2 3.9H4.4L17.8 20Z"/></svg>'
    return f'''<section class="section connect" id="contact" aria-labelledby="connect-title"><div class="connect-intro"><p class="eyebrow">Get in touch</p><h2 id="connect-title">Let’s connect.</h2><p>Ideas, projects, and life beyond the code.</p></div><div class="connect-grid"><div class="connect-platforms"><a class="connect-link" href="{E(config['twitter'])}" target="_blank" rel="noopener noreferrer"><span class="platform-icon">{x_icon}</span><span class="platform-copy"><strong>X / Twitter</strong><span>@LongbinLai</span></span><span class="platform-arrow" aria-hidden="true">↗</span></a><p class="connect-note">Follow along, or drop me a message.</p></div><div class="connect-qr"><div class="qr-copy"><p class="eyebrow">Xiaohongshu</p><h3>{E(config['xiaohongshu_name'])}</h3><p>Scan to follow my notes on AI and everyday life.</p><button class="qr-open text-link" type="button" aria-haspopup="dialog" aria-controls="qr-dialog">Enlarge QR code ↗</button></div><button class="qr-open qr-frame" type="button" aria-label="Enlarge Xiaohongshu QR code" aria-haspopup="dialog" aria-controls="qr-dialog"><span class="qr-window"><img src="{E(config['xiaohongshu_qr'])}" alt="Xiaohongshu QR code for Robin 同学 AI 生活" width="1279" height="1747" loading="lazy"></span></button></div></div><dialog id="qr-dialog" class="qr-dialog" aria-labelledby="qr-dialog-title"><div class="qr-dialog-head"><h2 id="qr-dialog-title">Find me on Xiaohongshu</h2><button class="qr-close" type="button" aria-label="Close QR code">×</button></div><img src="{E(config['xiaohongshu_qr'])}" alt="Xiaohongshu QR code for Robin 同学 AI 生活" width="1279" height="1747"><a class="text-link" href="{E(config['xiaohongshu_qr'])}" download="longbin-lai-xiaohongshu.jpeg">Save QR code ↓</a></dialog></section>'''

def graph():
    points=[(45,55),(150,28),(265,45),(320,120),(265,205),(145,220),(40,170),(175,120)]
    edges=[(0,1),(1,2),(2,3),(3,4),(4,5),(5,6),(6,0),(0,7),(1,7),(2,7),(3,7),(4,7),(5,7),(6,7),(0,5),(2,4)]
    return '<svg class="graph" viewBox="0 0 360 250" role="img" aria-label="Graph, vector, and full-text retrieval connected in one data engine">'+''.join(f'<line x1="{points[a][0]}" y1="{points[a][1]}" x2="{points[b][0]}" y2="{points[b][1]}"/>' for a,b in edges)+''.join(f'<circle cx="{x}" cy="{y}" r="{13 if i==7 else 6}" class="{"core" if i==7 else "node"}"/>' for i,(x,y) in enumerate(points))+'<text x="12" y="35">STRUCTURE</text><text x="265" y="25">SEMANTICS</text><text x="250" y="235">KEYWORDS</text></svg>'

def build():
    if OUT.exists(): shutil.rmtree(OUT)
    OUT.mkdir()
    shutil.copytree(ROOT/'static',OUT,dirs_exist_ok=True)
    shutil.copytree(ROOT/'web',OUT/'assets')
    shutil.copy(ROOT/'content/authors/admin/avatar.jpg',OUT/'assets/avatar.jpg')
    (OUT/'.nojekyll').touch()
    profile=read(ROOT/'content/authors/admin/_index.md')
    pubs,posts,projects=records('publication'),records('post'),records('project')
    for post in posts:
        translation = post['source'].with_name('index.zh.md')
        if translation.exists():
            zh_title = read(translation)['title']
            TEXT[post['title']] = zh_title
            TEXT[post['title'] + ' · Longbin (Robin) Lai'] = zh_title + ' · 赖龙彬'

    for kind in ['publication','post','project','talk','courses','slides']:
        for asset in (ROOT/'content'/kind).rglob('*'):
            if asset.is_file() and asset.suffix not in ['.md']:
                target=OUT/asset.relative_to(ROOT/'content'); target.parent.mkdir(parents=True,exist_ok=True);shutil.copy(asset,target)
    for d in pubs+posts+projects+records('talk')+records('courses')+records('slides'):
        if d['route'].startswith('/talk/'):
            body = f'<article class="page talk-detail"><a class="back" href="/talk/">← All talks</a><header class="talk-heading"><p class="eyebrow">Talks & courses</p><h1>{E(d["title"])}</h1><p class="talk-summary">{E(d.get("summary", ""))}</p>{talk_metadata(d)}</header><section class="talk-materials" aria-label="Presentation resources"><div><p class="eyebrow">Materials</p><h2>Explore this presentation</h2><p class="muted">Open the slides or course using the links below.</p></div>{resources(d)}</section><section class="prose talk-description"><h2>Overview</h2>{render(d["body"])}</section></article>'
            if d.get('presentation') or d.get('url_course'):
                is_course = bool(d.get('url_course'))
                source = d.get('presentation') or d['url_course']
                label = 'Course overview' if is_course else 'Interactive slides'
                link_label = 'Open course ↗' if is_course else 'Open presentation ↗'
                frame_title = 'Interactive course' if is_course else 'NeuG interactive presentation'
                hint = 'Explore the course outline, play each step, or open the course separately for a larger view.' if is_course else 'Click the presentation, then use ← / → to navigate. Press F for full screen.'
                extra_class = ' course-viewer' if is_course else ''
                viewer = f'<section class="presentation-viewer{extra_class}" aria-label="{frame_title}"><div class="presentation-toolbar"><span class="eyebrow">{label}</span><a class="text-link" href="{E(source)}" target="_blank" rel="noopener">{link_label}</a></div><iframe src="{E(source)}" title="{frame_title}" allow="fullscreen" allowfullscreen loading="eager"></iframe><p class="presentation-hint">{hint}</p></section>'
                body = re.sub(r'<section class="talk-materials".*?</section>', lambda match: viewer, body, count=1, flags=re.S)
                body = body.replace('class="page talk-detail"', 'class="page talk-detail has-presentation"')
            write(d['route'], d['title'], body)
            continue
        meta=str(d.get('publication','')) if d in pubs else str(d.get('date',''))[:10]
        body=f'<article class="page"><a class="back" href="/">← Home</a><p class="eyebrow" style="margin-top:30px">{E(d["route"].split("/")[1])}</p><h1>{E(d["title"])}</h1><div class="muted">{render(meta)}</div>'
        if d.get('authors'):body+=f'<p class="muted">{E(", ".join(("Longbin Lai" if d in pubs else "Longbin (Robin) Lai") if a == "admin" else str(a) for a in d["authors"]))}</p>'
        body+=resources(d)
        if d.get('abstract'): body+='<div class="prose"><h2>Abstract</h2>'+render(d['abstract'])+'</div>'
        body+='<div class="prose">'+render(d['body'])+'</div></article>'
        write(d['route'],d['title'],body)
    for p in (ROOT/'content/courses').rglob('*.md'):
        if p.name in ['index.md','_index.md']:continue
        d=read(p);route='/'+str(p.relative_to(ROOT/'content').with_suffix(''))+'/'
        write(route,d['title'],f'<article class="page"><a href="/">← Home</a><h1>{E(d["title"])}</h1><div class="prose">{render(d["body"])}</div></article>')
    for filename in ['privacy.md','terms.md']:
        d=read(ROOT/'content'/filename)
        write('/'+filename[:-3]+'/',d['title'],f'<article class="page"><h1>{E(d["title"])}</h1><div class="prose">{render(d["body"])}</div></article>')
    years=sorted({str(d['date'])[:4] for d in pubs},reverse=True)
    write('/publication/','Publications','<section class="page">'+section_head('Research archive','Publications')+'<p class="muted">Graph data management, distributed computing, and query optimization.</p><div class="filter"><input id="paper-search" type="search" aria-label="Search publications" placeholder="Search by title, author, or venue"><select id="paper-year" aria-label="Filter by year"><option value="">All years</option>'+''.join(f'<option>{y}</option>' for y in years)+'</select></div><p id="result-count" class="muted" role="status" aria-live="polite"></p>'+''.join(map(paper,pubs))+'<p id="no-results" class="empty" hidden>No matching publications. Try another title, author, or year.</p></section>')
    def writing(d):return f'<a class="writing-row" href="{d["route"]}"><time datetime="{str(d.get("date",""))[:10]}">{str(d.get("date",""))[:10]}</time><h3>{E(d["title"])}</h3><span aria-hidden="true">↗</span></a>'
    write('/post/','Writing','<section class="page">'+section_head('Notes & perspectives','Writing')+''.join(map(writing,posts))+'</section>')
    talk_rows = []
    for d in records('talk'):
        meta = str(d.get('date', ''))[:10] or 'Presentation materials'
        summary = d.get('summary', '')
        talk_rows.append(f'<article class="talk-entry"><p class="eyebrow">{E(meta)}</p><h2><a href="{d["route"]}">{E(d["title"])}</a></h2><p class="talk-location">{E(d.get("location", ""))}</p><p class="muted">{E(summary)}</p>{resources(d)}</article>')
    write('/talk/', 'Talks', '<section class="page">' + section_head('Presentations & materials', 'Talks') + '<p class="muted">Talks, courses, and presentation materials.</p>' + ''.join(talk_rows) + '</section>')
    names={'interactive':'GraphScope Interactive','gaia':'GAIA','gopt':'GOpt','glogs':'GLogS','patmat':'PatMat'}
    project_html=''
    for d in projects:
        name=names.get(d['source'].parent.name,d['title'])
        project_html+=f'<article class="project"><p class="eyebrow">{E(" / ".join(d.get("tags",[])[:2]))}</p><h3><a href="{d["route"]}">{E(name)} ↗</a></h3><p>{E(d.get("summary",""))}</p>{resources(d)}</article>'
    write('/project/','Projects','<section class="page">'+section_head('Open source & systems','Projects')+ '<div class="project-grid">'+project_html+'</div></section>')
    education=''.join(f'<li><strong>{E(c["course"])}</strong><span>{E(c["institution"])} · {c["year"]}</span></li>' for c in profile['education']['courses'])
    social='<div class="social"><a class="text-link" href="#contact">Connect ↗</a><a class="text-link" href="https://scholar.google.com/citations?user=iz2jcMYAAAAJ&amp;hl=en">Google Scholar ↗</a><a class="text-link" href="https://github.com/longbinlai">GitHub ↗</a><a class="text-link" href="/files/cv.pdf">CV ↗</a></div>'
    feature='<article class="feature"><div><p class="eyebrow">Featured open-source project</p><h3>NeuG</h3><p>A graph-native data engine for agentic applications. Graph, vector, and full-text retrieval over the same transactional data, embedded in your application or running as a service.</p><div class="social"><a class="text-link" href="https://neug.io/">Explore NeuG ↗</a><a class="text-link" href="https://github.com/alibaba/neug">Source code ↗</a></div></div>'+graph()+'</article>'
    body=f'''<section class="hero" aria-labelledby="intro-title"><div><p class="eyebrow">Researcher & engineer · Graphs / Data / AI</p><h1 id="intro-title">Longbin (Robin) Lai<span style="color:var(--accent)">.</span></h1><p class="lead">Building systems that make<br>connected data useful.</p><p class="intro">{E(profile['role'])} at {E(profile['organizations'][0]['name'])}. My work spans graph databases, distributed processing, query optimization, and applications of large language models.</p>{social}</div><img class="portrait" src="/assets/avatar.jpg" width="168" height="168" alt="Portrait of Longbin Lai"></section>
<section class="section" id="work">{section_head('01 / Engineering','Systems & open source','/project/','All projects')}{feature}<div class="project-grid">{project_html}</div></section>
<section class="section" id="research">{section_head('02 / Research','Selected publications','/publication/','All publications')} {''.join(paper(next(d for d in pubs if d['source'].parent.name==slug)) for slug in ['lyu-2025-sigmod','lai-2025-sigmod','graphscope-2024','lai-2023-atc','graphscope-nsdi'])}</section>
<section class="section" id="writing">{section_head('03 / Notes','Recent writing','/post/','All writing')}{''.join(map(writing,posts[:3]))}</section>
<section class="section" id="about">{section_head('04 / Background','A little about me')}<div class="about-grid"><div class="prose" style="margin:0">{render(profile['body'])}</div><div><p class="eyebrow" style="margin-bottom:24px">Education</p><ul class="education">{education}</ul><p class="eyebrow" style="margin-bottom:12px">Research interests</p><p class="muted">{' · '.join(map(E,profile['interests']))}</p></div></div></section>
{contact_section()}'''
    write('/','Research & Engineering',body)
    (OUT/'404.html').write_text(page('Page not found','<section class="page"><p class="eyebrow">404</p><h1>This page has moved.</h1><p>Explore the <a class="text-link" href="/publication/">publication archive</a> or <a class="text-link" href="/">return home</a>.</p></section>'))
    (OUT/'robots.txt').write_text(f'User-agent: *\nAllow: /\nSitemap: {BASE}/sitemap.xml\n')
    root=ET.Element('urlset',xmlns='http://www.sitemaps.org/schemas/sitemap/0.9')
    for route in ROUTES:ET.SubElement(ET.SubElement(root,'url'),'loc').text=BASE+route
    ET.ElementTree(root).write(OUT/'sitemap.xml',encoding='utf-8',xml_declaration=True)
    print(f'Built {len(ROUTES)} pages, {len(pubs)} publications, {len(posts)} posts, {len(projects)} projects → {OUT}')

if __name__=='__main__':build()
