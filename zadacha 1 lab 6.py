countries = {
    "Россия": "Москва",
    "США": "Вашингтон",
    "Канада": "Оттава",
    "Италия": "Рим",
    "Япония": "Токио",
    "Германия": "Берлин",
}
print(countries)

country1 = input("Введите страну: ")
print(countries[country1])

for country in sorted(countries):
    print(country, ":", countries[country])