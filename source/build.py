import base64, os
d = os.path.dirname(os.path.abspath(__file__))

def star(cx, cy, r):
    a, b = .08 * r, .32 * r
    f = lambda v: f"{v:.2f}".rstrip('0').rstrip('.')
    p = lambda x, y: f"{f(x)} {f(y)}"
    return (f"M{p(cx, cy-r)}C{p(cx+a, cy-b)} {p(cx+b, cy-a)} {p(cx+r, cy)}"
            f"C{p(cx+b, cy+a)} {p(cx+a, cy+b)} {p(cx, cy+r)}"
            f"C{p(cx-a, cy+b)} {p(cx-b, cy+a)} {p(cx-r, cy)}"
            f"C{p(cx-b, cy-a)} {p(cx-a, cy-b)} {p(cx, cy-r)}Z")

b64 = lambda f: base64.b64encode(open(os.path.join(d, f), 'rb').read()).decode()
s = open(os.path.join(d, 'src.html'), encoding='utf-8').read()
s = (s.replace('__PHOTOWEBP__', 'foto.webp').replace('__PHOTO__', 'foto.jpg')
      .replace('__CLAUDE__', 'data:image/png;base64,' + b64('claude.png'))
      .replace('__STARS__', '<path class="s1" d="%s"/><path class="s2" d="%s"/><path class="s3" d="%s"/>' % (star(33, 63, 32), star(75, 27, 20), star(79, 77, 12))))
open(os.path.join(d, 'index.html'), 'w', encoding='utf-8').write(s)
print(len(s))
