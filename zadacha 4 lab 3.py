import random
error_c = 0
c = 0
while error_c < 3:
    a = random.randint(0, 100)
    b = random.randint(0, 100)
    if int(input(f"{a} + {b} = ")) == a + b:
        c += 1
        print('Правильно!')
    else:
        error_c += 1
        print('Неправильно!')
print(f"Игра окончена. Правильных ответов {c}")