# Parent Class
class Animal:
    def speak(self):
        print("Animal speaks")

# Child Class (inherits from Animal)
class Dog(Animal):
    def speak(self):
        print("Dog barks")

dog = Dog()
dog.speak()  
