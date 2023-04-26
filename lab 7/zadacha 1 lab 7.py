from PIL import Image

image = Image.open('pig.png')

print("Размер изображения:", image.size)
print("Формат изображения:", image.format)
print("Цветовая модель изображения:", image.mode)

image.show()