class Person:
    def __init__(self, name, age):
        self._age = age  # Private variable (convention)

    @property
    def age(self):  # Getter method
        return self._age

    @age.setter
    def age(self, value):  # Setter method with validation
        if value < 0:
            raise ValueError("Age cannot be negative")
        self._age = value

person = Person("Alice", 30)
print(person.age)  # Calls getter -> Output: 30

person.age = 25  # Calls setter
print(person.age)  # Output: 25

# person.age = -5  # Raises ValueError: Age cannot be negative
