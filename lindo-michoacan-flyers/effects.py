# Variantes de los recortes: sticker (borde blanco) y duotono -> cutouts/
from PIL import Image, ImageFilter, ImageOps
def sticker(name, border=22):
    im = Image.open(f"cutouts/{name}.png")
    pad = border * 2
    im = ImageOps.expand(im, pad, fill=(0, 0, 0, 0))
    a = im.split()[3].point(lambda v: 255 if v > 40 else 0)
    a = a.filter(ImageFilter.MaxFilter(border * 2 + 1)).filter(ImageFilter.GaussianBlur(1.2))
    out = Image.new("RGBA", im.size, (255, 255, 255, 0)); out.putalpha(a)
    out.alpha_composite(im); out.save(f"cutouts/{name}-sticker.png")
def duotone(name, dark, light):
    im = Image.open(f"cutouts/{name}.png")
    g = ImageOps.autocontrast(im.convert("L"), cutoff=2)
    col = ImageOps.colorize(g, dark, light).convert("RGBA"); col.putalpha(im.split()[3])
    col.save(f"cutouts/{name}-duo-{dark.strip('#')}.png")
for n in ["coco", "cacahuate", "clasica", "duo"]: sticker(n)
duotone("clasica", "#1F5BE6", "#FFC2DA")
duotone("coco", "#2A1A13", "#FFC72C")
duotone("cacahuate", "#D7261E", "#FFF1C2")
