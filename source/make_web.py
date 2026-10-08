"""Genera ../index.html (pagina final) a partir de src.html, foto.jpg y claude.png."""
import os, subprocess, sys
d = os.path.dirname(os.path.abspath(__file__))
subprocess.run([sys.executable, os.path.join(d, 'build.py')], check=True)
tmp = os.path.join(d, 'index.html')
s = open(tmp, encoding='utf-8').read()
os.remove(tmp)
i = s.index('<svg width="0"')
head, body = s[:i], s[i:]
out = ('<!doctype html>\n<html lang="en" translate="no">\n<head>\n<meta charset="utf-8">\n'
       '<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">\n'
       '<meta name="google" content="notranslate">\n'
       '<meta name="color-scheme" content="light">\n'
       '<meta name="description" content="Alan Angelats, Lead Product Designer. Digital products and financial services.">\n'
       '<meta name="theme-color" content="#E7E0DA">\n'
       '<link rel="icon" href="favicon.svg" type="image/svg+xml">\n'
       '<link rel="icon" href="favicon.ico" sizes="48x48">\n'
       '<link rel="icon" href="favicon-32.png" sizes="32x32" type="image/png">\n'
       '<link rel="icon" href="favicon-16.png" sizes="16x16" type="image/png">\n'
       '<link rel="apple-touch-icon" href="apple-touch-icon.png">\n'
       '<link rel="manifest" href="manifest.webmanifest">\n' + head + '</head>\n<body>\n' + body + '\n</body>\n</html>\n')
open(os.path.join(d, '..', 'index.html'), 'w', encoding='utf-8').write(out)
