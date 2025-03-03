# thislist = ["apple", "banana", "cherry"]
# print(thislist)

# # Access items
# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[1])
# print(thislist[-1])
# print(thislist[2:5])
# print(thislist[:4])
# print(thislist[2:])
# print(thislist[-4:-1])

# # change items
# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
# thislist[1:3] = ["blackcurrant", "watermelon"]
# print(thislist)

# # Insert items
# thislist = ["apple", "banana", "cherry"]
# thislist.insert(2, "watermelon")
# print(thislist)

# # Add items
# thislist = ["apple", "banana", "cherry"]
# thislist.append("orange")
# print(thislist)

# # Insert
# thislist = ["apple", "banana", "cherry"]
# thislist.insert(1, "orange")
# print(thislist)

# # Extend
# thislist = ["apple", "banana", "cherry"]
# tropical = ["mango", "pineapple", "papaya"]
# thislist.extend(tropical)
# print(thislist)

# # remove
# thislist = ["apple", "banana", "cherry"]
# thislist.remove("banana")
# print(thislist)

# # remove with index
# thislist = ["apple", "banana", "cherry"]
# thislist.pop(1)
# print(thislist)
# thislist.pop()
# print(thislist)

# # delete
# thislist = ["apple", "banana", "cherry"]
# del thislist[0]
# print(thislist)

# # Clear
# thislist = ["apple", "banana", "cherry"]
# thislist.clear()
# print(thislist)

# Sort
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)
thislist.sort(reverse = True)
print(thislist)

# Copy
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)

thislist = ["apple", "banana", "cherry"]
mylist = thislist[:]
print(mylist)