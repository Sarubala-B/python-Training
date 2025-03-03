def add(a, b, c):
    return a + b + c

numbers = [1, 2, 3]
result = add(*numbers)  # Unpacks the list into individual arguments
print(result)  # Output: 6
