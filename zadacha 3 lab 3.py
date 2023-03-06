n = int(input("Введите количество слов: "))
s = ''
for i in range(n):
    s = str(input(""))
    if s.find("ф") != -1:
        print("Это редкое слово")
    else:
        print("Эх не очень редкое...")