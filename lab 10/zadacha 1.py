import json

with open("products.json", "r", encoding='utf-8') as f:
    d = json.load(f)

product = d["products"]

def print_products(product):
    print(f"Название: {product['name']}")
    print(f"Цена: {product['price']}")
    print(f"Вес: {product['weight']}")
    if product["available"]:
        print("В наличии")
    else:
        print("Нет в наличии")
    print()

list(map(print_products, product))