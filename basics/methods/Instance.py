class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age  # Instance attribute

    def introduce(self):
        return f"My name is {self.name} and I am {self.age} years old."

person1 = Person("Alice", 30)
print(person1.introduce())  # Output: My name is Alice and I am 30 years old.
