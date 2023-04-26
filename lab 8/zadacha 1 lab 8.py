from PIL import Image

image = Image.open("открытка.jpg")
place = (100, 150, 700, 1000)
cimg = image.crop(place)
cimg.save("обрезанная открытка.jpg")