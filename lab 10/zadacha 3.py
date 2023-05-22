eng_rus_dict = {}
with open('en-ru.txt', 'r', encoding='utf-8') as file:
    for line in file:
        line = line.strip()
        if line:
            eng_word, ru_translations = line.split(' - ')
            ru_words = ru_translations.split(', ')
            for ru_word in ru_words:
                eng_rus_dict[ru_word] = eng_word

with open('ru-en.txt', 'w', encoding='utf-8') as file:
    for ru_word in sorted(eng_rus_dict):
        eng_word = eng_rus_dict[ru_word]
        file.write(f'{ru_word} - {eng_word}\n')