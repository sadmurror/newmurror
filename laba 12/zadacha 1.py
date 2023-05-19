class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Название ресторана: {self.restaurant_name}")
        print(f"Тип кухни: {self.cuisine_type}")

    def open_restaurant(self):
        print("Ресторан открыт")

class IceCreamStand(Restaurant):

    def __init__(self, restaurant_name, cuisine_type, flavors):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors

    def display_flavors(self):
        print("Список сортов мороженого:")
        for flavor in self.flavors:
            print("- " + flavor)

ice_cream_stand = IceCreamStand("MURROR", "кафе-мороженое", ["ванильное", "клубника", "шоколад", "фисташковое"])
ice_cream_stand.display_flavors()