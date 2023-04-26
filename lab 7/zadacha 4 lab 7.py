from PIL import Image, ImageDraw, ImageFont
import os

if not os.path.exists("watermark"):
    os.makedirs("watermark")

image = Image.open("pig.png")
font = ImageFont.truetype("Minecraft.ttf", 30)
pencil = ImageDraw.Draw(image)
pencil.text((10, 100), "myaa", font=font, fill="blue")
image.save("watermark/pigwatermark.png")
