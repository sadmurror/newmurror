import tkinter as tk

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
        return self.flavors

icecream = IceCreamStand("MURROR", "кафе-мороженое", ["ванильное", "клубничное", "шоколадное", "фисташковое"], "центр города", "10:00 - 20:00")

window = tk.Tk()
window.title("MURROR: список вкусов мороженого")
label = tk.Label(window, text = "\n".join((icecream.display_flavors())), font = ("Arial Bold", 25))
label.grid(column=0, row=0)
window.mainloop()




