s = ""
a = ""
while not "stop" in a:
    s += str(input("Введите слово: "))
    s += " "
    a = str(input("Введите stop если хотите закончить: "))
print(s)