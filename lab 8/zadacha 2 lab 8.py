from PIL import Image

cel = {
    "День Рождения": "день рождения.jpg",
    "День победы": "9 мая.jpg",
    "Новый год": "новый год.jpg",
    "Пасха": "пасха.jpg"
}

celebrity = input("Напишите праздник: ")
pcel = cel.get(celebrity)
if pcel:
    image = Image.open(pcel)
    image.show()
else:
    print("Такой открытки у меня нет :(")