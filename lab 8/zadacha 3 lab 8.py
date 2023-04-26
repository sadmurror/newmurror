from PIL import Image, ImageDraw, ImageFont

image = Image.open("открытка.jpg")
pencil = ImageDraw.Draw(image)
font1 = ImageFont.truetype("Krivulya.ttf", 48)
font2 = ImageFont.truetype("SensalOutline.ttf", 48)
color1 = (200, 0, 30)
color2 = (0, 255, 0)
name = input("Для кого открыточка? ")
nametxt = name + ", поздравляю!"
iwid, ihei = image.size
txtw, txth = pencil.textsize(nametxt, font2)
x = (iwid - txtw) // 2
y = ihei - txth - 10

pencil.text((x + 300, y - 30), name, color1, font2)
pencil.text((x + txtw - pencil.textsize(", поздравляю!", font1)[0], y), ", поздравляю!", color2, font1)

image.show()
image.save("result.png")