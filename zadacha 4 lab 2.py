colors = ("красный", "синий", "жёлтый")
color1 = input()
color2 = input()

if color1 in colors and color2 in colors:
    if color1 != color2:
        if (color1 in ("красный","синий")) and (color2 in ("красный","синий")):
            print("фиолетовый")
        if (color1 in ("красный","жёлтый")) and (color2 in ("красный","жёлтый")):
            print("оранжевый")
        if (color1 in ("синий","жёлтый")) and (color2 in ("синий","жёлтый")):
            print("зелёный")
    else:
        print(color1)
else:
    print("ошибка")


