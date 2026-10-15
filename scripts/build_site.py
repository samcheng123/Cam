#!/usr/bin/env python3
"""Generate the static academic website. Run from any directory with Python 3."""
import html
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = '/Cam/'
URL = 'https://samcheng123.github.io'
PUBLICATIONS = json.loads((ROOT / '_data/publications.json').read_text())
FIGURES = json.loads((ROOT / '_data/figure-sources.json').read_text())
SELECTED = ['C5', 'C6', 'J4', 'C2', 'C1', 'J1']

def esc(value):
    return html.escape(str(value), quote=True)

def link(url, text):
    return f'<a href="{esc(url)}">{text}</a>'

def page(title, content, current='about', slug='', description=None):
    description = description or 'Chun Wun (Sam) Cheng — PhD student at the University of Cambridge. Machine learning, neural operators, scientific computing and medical imaging.'
    navigation = ''.join(f'<a href="{BASE}{path}"' + (' aria-current="page"' if key == current else '') + f'>{label}</a>' for key, path, label in [('about','','about'),('publications','publications/','publications'),('activities','activities/','activities'),('vitae','site-assets/CV_Sam_Cheng.pdf','vitae ↗')])
    structured = json.dumps({'@context':'https://schema.org','@type':'Person','name':'Chun Wun (Sam) Cheng','url':URL+BASE,'image':URL+BASE+'site-assets/profile.JPG','affiliation':{'@type':'CollegeOrUniversity','name':'University of Cambridge'},'sameAs':['https://scholar.google.com/citations?user=Qsckv9wAAAAJ','https://github.com/samcheng123']},ensure_ascii=False)
    return f'''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <title>{esc(title)} | Sam Cheng</title>
  <meta name="description" content="{esc(description)}">
  <meta name="theme-color" content="#ffffff">
  <link rel="canonical" href="{URL}{BASE}{slug}">
  <meta property="og:type" content="website">
  <meta property="og:title" content="{esc(title)} | Sam Cheng">
  <meta property="og:description" content="{esc(description)}">
  <meta property="og:url" content="{URL}{BASE}{slug}">
  <meta property="og:image" content="{URL}{BASE}site-assets/profile.JPG">
  <link rel="icon" href="{BASE}site-assets/favicon.svg" type="image/svg+xml">
  <link rel="stylesheet" href="{BASE}site-assets/site.css">
  <script src="{BASE}site-assets/site.js" defer></script>
  <script type="application/ld+json">{structured}</script>
</head>
<body id="top">
  <a class="skip-link" href="#main">Skip to content</a>
  <header class="site-header"><div class="nav-wrap">
    <a class="wordmark" href="{BASE}"><strong>Sam</strong> Cheng</a>
    <button class="menu-toggle" type="button" aria-label="Toggle navigation" aria-expanded="false" aria-controls="navigation">menu ☰</button>
    <nav class="nav-links" id="navigation" aria-label="Main navigation">{navigation}</nav>
  </div></header>
  <main class="container" id="main">{content}</main>
  <footer class="site-footer"><div class="footer-inner">
    <p>© 2026 Chun Wun (Sam) Cheng · Updated October 2026</p>
    <div class="footer-links"><a href="mailto:cwc56@cam.ac.uk">email</a><a href="https://scholar.google.com/citations?user=Qsckv9wAAAAJ">scholar</a><a href="https://github.com/samcheng123">github</a></div>
  </div></footer>
</body>
</html>
'''

def paper_html(p, selected=False):
    title = esc(p['title'])
    resources = p.get('links', [])
    title = link(resources[0]['url'], title) if resources else title
    authors = ', '.join(f'<span class="author-self">{esc(a)}</span>' if ('Cheng' in a and ('Chun' in a or 'C. W.' in a)) else esc(a) for a in p['authors'])
    venue = p['venue']
    if p.get('year') and str(p['year']) not in venue:
        venue += ' · ' + str(p['year'])
    links = ''.join(link(r['url'], esc(r['label'])) for r in resources)
    figure = ''
    if selected:
        figure = f'<a class="paper-figure" href="{BASE}site-assets/figures/{p["id"]}.webp" aria-label="View figure for {esc(p["title"])}"><img src="{BASE}site-assets/figures/{p["id"]}.webp" alt="{esc(FIGURES[p["id"]]["alt"])}" width="{FIGURES[p["id"]]["web_dimensions"][0]}" height="{FIGURES[p["id"]]["web_dimensions"][1]}" loading="lazy" decoding="async"></a>'
    distinction = f'<p class="distinction">{esc(p["distinction"])}</p>' if p.get('distinction') else ''
    description = f'<p class="paper-description">{esc(p["description"])}</p>' if selected and p.get('description') else ''
    return f'''<article class="publication{' with-figure' if selected else ''}" id="{esc(p['id'])}" data-publication data-category="{esc(p['category'])}">
      {figure}<div class="paper-body"><h3>{title}</h3><p class="authors">{authors}</p><p class="venue">{esc(venue)}</p>{distinction}<div class="paper-links">{links}</div>{description}</div>
    </article>'''

def write(relative, content):
    path = ROOT / relative
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content)

by_id = {p['id']:p for p in PUBLICATIONS}
home = '''<section aria-labelledby="profile-name">
  <h1 id="profile-name">Chun Wun (<strong>Sam</strong>) Cheng</h1>
  <p class="subtitle">PhD Student · University of Cambridge · SNSF Scholar</p>
  <div class="intro">
    <figure class="portrait"><img src="/Cam/site-assets/profile.JPG" alt="Portrait of Chun Wun (Sam) Cheng" width="1684" height="2105" fetchpriority="high"></figure>
    <p>I am a PhD student in Mathematics of Information at the <a href="https://www.cam.ac.uk/">University of Cambridge</a>, in the Department of Applied Mathematics and Theoretical Physics. I am supervised by <a href="https://www.damtp.cam.ac.uk/person/cbs31">Carola-Bibiane Schönlieb</a> and <a href="https://angelicaiaviles.wordpress.com/">Angelica I. Aviles-Rivero</a>, and supported by a four-year Swiss National Science Foundation scholarship.</p>
    <p>My research lies at the intersection of <strong>machine learning, scientific computing, and computational physics</strong>. I develop scalable and robust methods for solving partial differential equations, with a particular interest in neural operators and continuous-depth models.</p>
    <p>I also work on medical imaging, diffusion models, and vision-language learning. Previously, I was a research intern in the BBC Computer Vision Team and a visiting student at Tsinghua University’s Yau Mathematical Sciences Center.</p>
    <p>For research discussions and collaborations, please get in touch at <a href="mailto:cwc56@cam.ac.uk">cwc56@cam.ac.uk</a>.</p>
  </div>
  <div class="contact-links" aria-label="Profile links"><a href="mailto:cwc56@cam.ac.uk">email</a><a href="https://scholar.google.com/citations?user=Qsckv9wAAAAJ">Google Scholar</a><a href="https://github.com/samcheng123">GitHub</a><a href="/Cam/site-assets/CV_Sam_Cheng.pdf">curriculum vitae ↗</a></div>
</section>
<section class="section" aria-labelledby="news-heading">
  <h2 id="news-heading">news</h2>
  <dl class="news-list">
    <div class="news-item"><dt>2026</dt><dd><a href="/Cam/publications/#C5">ProSMA-UNet</a> and <a href="/Cam/publications/#C6">MAP-Diff</a> accepted for <strong>oral presentations at MICCAI 2026</strong>.</dd></div>
    <div class="news-item"><dt>Jul 2026</dt><dd>Co-organised <em>Data, Models, and Gradients: Learning to Optimise — and Beyond</em> at SIAM Optimization, Edinburgh.</dd></div>
    <div class="news-item"><dt>Jun 2026</dt><dd>Co-organised the <em>AI4Science Beijing Meetup: Learned Partial Differential Equations</em> at Tsinghua University.</dd></div>
    <div class="news-item"><dt>2025</dt><dd><a href="/Cam/publications/#J4">Mamba Neural Operator</a> accepted by the <em>Journal of Computational Physics</em>.</dd></div>
    <div class="news-item"><dt>2025</dt><dd><a href="/Cam/publications/#C1">Cross-Modal Few-Shot Learning with Second-Order Neural ODEs</a> accepted for an <strong>oral presentation at AAAI 2025</strong>.</dd></div>
  </dl>
</section>
<section class="section divided" aria-labelledby="selected-heading">
  <div class="section-header"><h2 id="selected-heading">selected publications</h2><a href="/Cam/publications/">all publications →</a></div>
'''
home += '\n'.join(paper_html(by_id[i], True) for i in SELECTED)
home += '''<p class="equal-note">* Equal contribution.</p></section>
<section class="section divided" aria-labelledby="beyond-heading"><h2 id="beyond-heading">beyond research</h2>
<p>I enjoy teaching and mentoring students, and helping bring the research community together through workshops and tutorials. Outside research, I play volleyball and previously competed with Wah Ching in Hong Kong.</p>
<p><a href="/Cam/activities/">Teaching, experience, and academic service →</a></p></section>'''
write('index.html',page('About', home))

publications = '''<h1>publications</h1>
<p class="page-intro">Neural operators, scientific machine learning, medical imaging, and vision-language learning.</p>
<p class="pub-summary"><strong>23 papers</strong> · 5 journal papers · 6 conference papers · 12 under review</p>
<div class="publication-tools"><label class="search-label" for="publication-search">Search by title, author, venue, or year</label><input class="search-input" id="publication-search" type="search" placeholder="Search publications…" autocomplete="off">
<div class="filter-buttons" role="group" aria-label="Filter publications"><button type="button" data-filter="all" aria-pressed="true">All (23)</button><button type="button" data-filter="journal" aria-pressed="false">Journals (5)</button><button type="button" data-filter="conference" aria-pressed="false">Conferences (6)</button><button type="button" data-filter="preprint" aria-pressed="false">Under review (12)</button></div><p class="results-status" id="results-status" role="status" aria-live="polite">23 of 23 publications</p></div>
<p class="equal-note">* Equal contribution. Manuscripts under review are listed separately below.</p>
'''
for category, heading in [('journal','journal papers'),('conference','conference papers'),('preprint','under review')]:
    publications += f'<section class="publication-group" id="{category}"><h2>{heading}</h2>'
    publications += '\n'.join(paper_html(p) for p in PUBLICATIONS if p['category'] == category)
    publications += '</section>'
publications += '<p class="empty-state" id="empty-state" hidden>No publications match your search. Try a different keyword or category.</p><p class="back-to-top"><a href="#top">back to top ↑</a></p>'
write('publications/index.html',page('Publications',publications,'publications','publications/'))

activities = '''<div class="activities"><h1>activities &amp; experience</h1><p class="page-intro">Research, teaching, and the communities I contribute to.</p><nav class="jump-links" aria-label="Activities sections"><a href="#education">education</a><a href="#experience">experience</a><a href="#teaching">teaching</a><a href="#service">service</a><a href="#talks">talks</a><a href="#mentorship">mentorship</a><a href="#honors">honors</a></nav>'''
activities += (ROOT / '_data/activities.html').read_text()
activities += '<p class="back-to-top"><a href="#top">back to top ↑</a></p></div>'
write('activities/index.html',page('Activities & experience',activities,'activities','activities/'))
cv = '''<h1>curriculum vitae</h1><p class="page-intro">Chun Wun (Sam) Cheng · October 2026</p><p>My full academic CV includes publications, research and teaching experience, awards, talks, and professional activities.</p><a class="cv-download" href="/Cam/site-assets/CV_Sam_Cheng.pdf">Open CV (PDF) ↗</a><p>Browse <a href="/Cam/publications/">publications</a> or <a href="/Cam/activities/">activities and experience</a> on this website.</p>'''
write('cv/index.html',page('Curriculum vitae',cv,'vitae','cv/'))
write('404.html',page('Page not found','<h1>page not found</h1><p>This page may have moved. Visit my <a href="/Cam/">homepage</a>, <a href="/Cam/publications/">publications</a>, or <a href="/Cam/activities/">activities</a>.'))
write('sitemap.xml','<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+''.join(f'<url><loc>{URL}{BASE}{p}</loc><lastmod>2026-10-15</lastmod></url>' for p in ['', 'publications/', 'activities/', 'cv/'])+'</urlset>\n')
write('robots.txt','User-agent: *\nAllow: /\nSitemap: '+URL+BASE+'sitemap.xml\n')
print('Generated homepage, publications, activities, CV, 404, sitemap, and robots.txt.')
