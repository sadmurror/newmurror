from PIL import Image, ImageFilter
import os


if not os.path.exists("changed"):
    os.makedirs("changed")

for i in range(1, 6):
    image = Image.open(f"source/{i}.jpg")
    image.filter(ImageFilter.EMBOSS).save(f"changed/{i}.jpg")
    image.close()