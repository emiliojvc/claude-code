# Recorta el fondo de las fotos de paletas (rembg) -> cutouts/*.png
import sys
from rembg import remove, new_session
from PIL import Image
s = new_session(sys.argv[1] if len(sys.argv) > 1 else "isnet-general-use")
for n in ["coco", "cacahuate", "clasica", "duo"]:
    im = Image.open(f"assets/{n}.jpg")
    out = remove(im, session=s, post_process_mask=True)
    out.crop(out.getbbox()).save(f"cutouts/{n}.png")
    print(n, out.getbbox())
