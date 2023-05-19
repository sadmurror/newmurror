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

    def __init__(self, restaurant_name, cuisine_type, flavors, location, worktime):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors
        self.location = location
        self.worktime = worktime

    def display_flavors(self):
        print("Список сортов мороженого:")
        for flavors in self.flavors:
            print("- " + flavors)

    def remove_flavor(self, flavors):
        self.flavors.remove(flavors)

    def add_flavor(self, flavors):
        self.flavors.append(flavors)

    def has_flavor(self, flavors):
        if flavors in self.flavors:
            print("Такой вкус есть!")
        else:
            print("Такого вкуса нет!")

class IceCreamInCup(IceCreamStand):

    def __init__(self, restaurant_name, cuisine_type, flavors, location, worktime, cup_material):
        super().__init__(restaurant_name, cuisine_type, flavors, location, worktime)
        self.cup_material = cup_material

    def print_cup_material(self):
        print(f"Из какого материала стаканчик: {self.cup_material}")

class IceCreamCut(IceCreamStand):

    def __init__(self, restaurant_name, cuisine_type, flavors, location, worktime, pieces):
        super().__init__(restaurant_name, cuisine_type, flavors, location, worktime)
        self.pieces = pieces

    def print_pieces(self):
        print(f"На сколько частей разрезать: {self.pieces}")

incup = IceCreamInCup("MURROR", "кафе-мороженое", ["клубничное", "шоколадное"], "центр города", "10:00 - 20:00", "вафельное")
incup.print_cup_material()

icecream_peaces = IceCreamCut("MURROR", "кафе-мороженое", ["фисташковое", "шоколадное", "ванильное"], "центр города", "10:00 - 21:00", 4)
icecream_peaces.print_pieces()

