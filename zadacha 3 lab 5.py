days = ("Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье")
weekend = int(input("сколько выходных вы хотите? "))
wend_days = days[-weekend:]
wdays = days[:-weekend]
print("Ваши выходные дни:", ", ".join(wend_days))
print("Ваши рабочие дни:", ", ".join(wdays))