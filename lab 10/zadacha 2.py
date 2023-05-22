import json

with open("products.json", "r", encoding="utf-8") as f:
    d = json.load(f)

name = input("Введите название продукта: ")
price = int(input("Введите цену продукта: "))
weight = int(input("Введите вес продукта: "))
available = input("В наличии? [Да/Нет]: ").lower() == "да"

nproducts = {
    "name": name,
    "price": price,
    "weight": weight,
    "available": available
}
d["products"].append(nproducts)

with open("products.json", "w", encoding="utf-8") as json_file:
    json.dump(d, f)

for product in d["products"]:
    print("Название: " + product["name"])
    print("Цена: " + str(product["price"]))
    print("Вес: " + str(product["weight"]))
    if product["available"]:
        print("В наличии")
    else:
        print("Нет в наличии")
    print()