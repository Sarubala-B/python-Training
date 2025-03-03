class Person:
    species = "Human"  # Class attribute

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def set_species(cls, species_name):
        cls.species = species_name  # Modifies class-level attribute

print(Person.species)  # Output: Human
Person.set_species("Homo sapiens")
print(Person.species)  # Output: Homo sapiens
