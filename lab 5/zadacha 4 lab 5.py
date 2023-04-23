import random

g1 = ["Иванов", "Петров", "Сидоров", "Смирнов", "Козлов","Николаев","Егоров","Анисимов","Александров","Алексеев"]
g2 = ["Кузнецов", "Попов", "Васильев", "Морозов", "Федоров","Фролов","Исаев","Максимов","Воронов","Зайцев"]

steam = random.sample(g1, 5) + random.sample(g2, 5)

print("Группа 1:", g1)
print("Группа 2:", g2)
print("Спортивная команда:", steam)
print("Длина списка:", len(steam))

sortteam = sorted(steam)

surname = "Иванов"
if surname in sortteam:
    print(f"Фамилия {surname} есть в команде")
    print(f"Он встречается {sortteam.count(surname)} раз(a)")
else:
    print(f"Фамилия {surname} не найдена в команде")