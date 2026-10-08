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
       '<meta name="theme-color" content="#E7E0DA">\n' + head + '</head>\n<body>\n' + body + '\n</body>\n</html>\n')
open(os.path.join(d, '..', 'index.html'), 'w', encoding='utf-8').write(out)
