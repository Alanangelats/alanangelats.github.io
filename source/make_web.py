"""Genera ../index.html (pagina final) a partir de src.html, foto.jpg y claude.png."""
import os, shutil, json, subprocess, sys
d = os.path.dirname(os.path.abspath(__file__))
subprocess.run([sys.executable, os.path.join(d, 'build.py')], check=True)
root = os.path.join(d, '..')
# foto: JPG a calidad alta + WebP casi sin pérdida, servidas como archivos (HTML mucho más ligero)
shutil.copyfile(os.path.join(d, 'foto.jpg'), os.path.join(root, 'foto.jpg'))
try:
    from PIL import Image
    Image.open(os.path.join(d, 'foto.jpg')).convert('RGB').save(os.path.join(root, 'foto.webp'), 'WEBP', quality=95, method=6)
except Exception as e:
    print('aviso: no se pudo generar foto.webp', e)
tmp = os.path.join(d, 'index.html')
s = open(tmp, encoding='utf-8').read()
os.remove(tmp)

URL = 'https://alanangelats.github.io/'
TITLE = 'Alan Angelats | Lead Product Designer in Madrid \u00b7 Digital Banking & AI'
DESC = 'Lead Product Designer in Madrid with 20+ years designing digital banking and financial products, with AI and Design Systems. Experience, skills and clients.'
LD = {"@context": "https://schema.org", "@graph": [
  {"@type": "WebSite", "@id": URL + "#website", "url": URL, "name": "Alan Angelats", "inLanguage": ["en", "es"]},
  {"@type": "Person", "@id": URL + "#alan", "name": "Alan Angelats", "url": URL, "image": URL + "foto.jpg",
   "jobTitle": "Lead Product Designer", "description": DESC,
   "address": {"@type": "PostalAddress", "addressLocality": "Madrid", "addressCountry": "ES"},
   "worksFor": {"@type": "Organization", "name": "EGGS, Part of Sopra Steria"},
   "alumniOf": {"@type": "CollegeOrUniversity", "name": "Universitat Oberta de Catalunya"},
   "knowsLanguage": ["English", "Spanish", "Catalan"],
   "knowsAbout": ["Product Design", "UX/UI", "Design Systems", "AI Product Design", "UX Research", "Service Design", "Digital Banking", "Accessibility"]}]}
i = s.index('<svg width="0"')
head, body = s[:i], s[i:]
out = ('<!doctype html>\n<html lang="en" translate="no">\n<head>\n<meta charset="utf-8">\n'
       '<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">\n'
       '<meta name="google" content="notranslate">\n'
       '<meta name="color-scheme" content="light">\n'
       '<meta name="description" content="' + DESC + '">\n'
       '<meta name="robots" content="index,follow,max-image-preview:large">\n'
       '<link rel="canonical" href="' + URL + '">\n'
       '<meta property="og:type" content="website">\n<meta property="og:site_name" content="Alan Angelats">\n'
       '<meta property="og:title" content="' + TITLE.replace('&', '&amp;') + '">\n<meta property="og:description" content="' + DESC + '">\n'
       '<meta property="og:url" content="' + URL + '">\n<meta property="og:image" content="' + URL + 'og-image.jpg">\n'
       '<meta property="og:image:width" content="1200">\n<meta property="og:image:height" content="630">\n'
       '<meta property="og:image:alt" content="Alan Angelats, Lead Product Designer in Madrid">\n'
       '<meta property="og:locale" content="en_US">\n<meta property="og:locale:alternate" content="es_ES">\n'
       '<meta name="twitter:card" content="summary_large_image">\n<meta name="twitter:title" content="' + TITLE.replace('&', '&amp;') + '">\n'
       '<meta name="twitter:description" content="' + DESC + '">\n<meta name="twitter:image" content="' + URL + 'og-image.jpg">\n'
       '<link rel="preload" as="image" href="foto.webp" type="image/webp" fetchpriority="high">\n'
       '<script type="application/ld+json">' + json.dumps(LD, ensure_ascii=False, separators=(',', ':')) + '</script>\n'
       '<meta name="theme-color" content="#E7E0DA">\n'
       '<link rel="icon" href="favicon.svg" type="image/svg+xml">\n'
       '<link rel="icon" href="favicon.ico" sizes="48x48">\n'
       '<link rel="icon" href="favicon-32.png" sizes="32x32" type="image/png">\n'
       '<link rel="icon" href="favicon-16.png" sizes="16x16" type="image/png">\n'
       '<link rel="apple-touch-icon" href="apple-touch-icon.png">\n'
       '<link rel="manifest" href="manifest.webmanifest">\n' + head + '</head>\n<body>\n' + body + '\n</body>\n</html>\n')
open(os.path.join(d, '..', 'index.html'), 'w', encoding='utf-8').write(out)
