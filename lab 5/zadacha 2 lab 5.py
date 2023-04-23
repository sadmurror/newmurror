s = ["аквамарин", "кварц", "изумруд", "рубин", "сапфир", "янтарь", "обсидиан"]
set1 = set(s)
if len(s) != len(set1):
    for gemstone in set1:
        if s.count(gemstone) > 1:
            print("есть повторы: ", gemstone)
else:
    print("повторов нет")