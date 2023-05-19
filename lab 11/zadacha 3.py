class Restaurant:

    def __init__(self, restaurant_name, cuisine_type, rating):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.rating = rating

    def describe_restaurant(self):
        print(f"Название ресторана: {self.restaurant_name}")
        print(f"Тип кухни: {self.cuisine_type}")
        print(f"Рейтинг: {self.rating}")

    def open_restaurant(self):
        print("Ресторан открыт!")

    def rating_update(self, rating):
        self.rating = rating
        print(f"Нынешний рейтинг: {self.rating}")

restaurant1 = Restaurant("MURROR", "италянская кухня", "4.9")

restaurant1.describe_restaurant()
restaurant1.rating_update("5")