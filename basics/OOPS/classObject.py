# Defining a class
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_info(self):
        print(f"Car: {self.brand} {self.model}")

# Creating an object
car1 = Car("Toyota", "Camry")
car1.display_info()  # Output: Car: Toyota Camry
