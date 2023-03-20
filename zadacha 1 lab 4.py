def proverka(x):
    if x % 3 == 0:
        print("Число делится на 3")
        return None
    else:
        print("Число не делится на 3")
        return None

b = int(input("Введите число: "))
num = float(b)
res = proverka(num)
if res is not None:
    print(res)