add = lambda x, y: x + y
print(add(3, 5))  
 

numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
print(squared)  


students = [("Alice", 25), ("Bob", 20), ("Charlie", 23)]
sorted_students = sorted(students, key=lambda x: x[1])  # Sort by age
print(sorted_students)  
