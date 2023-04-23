seat = int(input("Введите номер места (от 1 до 54): "))

if seat > 54:
    print("ошибка")
elif seat > 36:
    print("боковое")
elif n % 2:
    print("в купе внизу")
else:
    print("в купе вверху")

