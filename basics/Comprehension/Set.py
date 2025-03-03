a = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7]

res = {num for num in a if num % 2 == 0}
print(res)


res = {num**2 for num in range(1, 6)}
print(res)
