#  Object Initialization: 
class Person:
    def __init__(self, name, age):  # Constructor
        self.name = name
        self.age = age

p = Person("Alice", 25)
print(p.name, p.age) 

# String Representation
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Person: {self.name}, {self.age}"

    def __repr__(self):
        return f"Person('{self.name}', {self.age})"

p = Person("Alice", 25)
print(str(p)) 
print(repr(p))


# Operator Overloading
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

p1 = Point(2, 3)
p2 = Point(4, 5)
p3 = p1 + p2  # Calls p1.__add__(p2)
print(p3.x, p3.y) 


#  Length and Indexing
class Team:
    def __init__(self, members):
        self.members = members

    def __len__(self):
        return len(self.members)

team = Team(["Alice", "Bob", "Charlie"])
print(len(team)) 

class Team:
    def __init__(self, members):
        self.members = members

    def __getitem__(self, index):
        return self.members[index]

team = Team(["Alice", "Bob", "Charlie"])
print(team[1]) 


# Comparisons
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):  
        return self.age == other.age

p1 = Person("Alice", 25)
p2 = Person("Bob", 25)
print(p1 == p2)  


#  Callable Objects
class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, value):
        return self.factor * value

double = Multiplier(2)
print(double(10))  
