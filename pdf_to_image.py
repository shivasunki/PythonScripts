import fitz
from PIL import Image

pdffile = "<Please replace your path here>"
doc = fitz.open(pdffile)
page = doc.load_page(0)  # number of page
zoom = 2    # zoom factor
mat = fitz.Matrix(zoom, zoom)

pix = page.get_pixmap(matrix=mat, dpi=300)

img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)

output = "out10Oct23.jpg"

#Without using pillow image
#pix.save(output)

img.save(output, "JPEG")
doc.close()