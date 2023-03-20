def lucky(num):
    hlf = len(num) // 2
    fhlf = num[:hlf]
    sechlf = num[hlf:]
    return sum(map(int,fhlf)) == sum(map(int,sechlf))
num = input("введите номер билета: ")
if len(num) % 2 == 0:
    if lucky(num):
        print("счастливый билет")
    else:
        print("несчастливый билет")
else:
    print("номер должен быт четной длины")
