class Car:
    def __init__(self, brand, model):
        self.brand = brand  # Instance Variable
        self.model = model

    # def display_info(self):
    #     return f"{self.brand} {self.model}"

    def __repr__(self):
        return f"{self.brand} {self.model}"
    
    def __iter__(self):
        for i in [self.brand,self.model]:
            yield i
    

# Creating an object (instance)
car1 = Car("Toyota", "Corolla")
print(car1) 
print (Car) # Output: Toyota Corolla

for i in car1:
    print (i)
