students = {
    "Иванов": {"испанский", "немецкий", "японский"},
    "Зубцова": {"китайский", "английский", "итальянский", "немецкий"},
    "Степанова": {"итальянский", "французский", "китайский"},
    "Дмитриева": {"английский", "китайский", "японский"},
    "Лебедева": {"корейский", "китайский", "японский", "английский"},
}

all_languages = set()
for languages in students.values():
    all_languages.update(languages)

print("Сколько языков знают студенты", len(all_languages))
print("Отсортированный список языков", sorted(all_languages))

chin = []
for student, languages in students.items():
    if "китайский" in languages:
        chin.append(student)

print("Список студентов, которые знают китайский язык:", chin)