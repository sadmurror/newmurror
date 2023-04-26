from PIL import Image

image = Image.open("cookie.jpg")

resize = image.resize((int(image.width/3), int(image.height/3)))
resize.save("resize.jpg")

horiz = image.transpose(Image.FLIP_LEFT_RIGHT)
horiz.save("horiz.jpg")

vertical = image.transpose(Image.FLIP_TOP_BOTTOM)
vertical.save("vertical.jpg")
