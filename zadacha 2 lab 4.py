def proverka(x):
    try:
        return 100/x
    except ValueError:
        print("Вы ввели не число")
        return None
    except ZeroDivisionError:
        print("На нол не делится")
        return None
b = input("Введите число: ")

try:
    num = float(b)
except ValueError:
    print("Вы ввели не число")
else:
    res = proverka(num)
    if res is not None:
        print("100 / {} = {}".format(num,res))
