res = {num: num**3 for num in range(1, 6)}
print(res)

a = ["Texas", "California", "Florida"] # states
b = ["Austin", "Sacramento", "Tallahassee"] # capital

res = {state: capital for state, capital in zip(a, b)}
print(res)
