from PIL import Image


# For single image to pdf
pdf_path = "output.pdf"
img_path = "outfile.png"

image = Image.open(img_path)

image.save(pdf_path)

# For multiple images
images_path = "images_path\\"
pdf_path = "pdf_path.pdf"
images = []
for i in images_path:
  images.append(Image.open(i))
images[0].save(pdf_path, save_all=True, append_images=images[1:])