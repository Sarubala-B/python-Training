res = (num for num in range(10) if num % 2 == 0)
print(list(res))
 

res = (num**2 for num in range(1, 6))
print(tuple(res))
