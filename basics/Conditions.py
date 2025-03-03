# # If statements
# x = 20
# if x > 30:
#     print("x is greater than 30")
# elif x > 10:
#     print("x is greater than 10 but less than or equal to 30")  # Output
# else:
#     print("x is 10 or less")

# # For
# fruits = ["apple", "banana", "cherry"]
# for fruit in fruits:
#     print(fruit)

# # Range 
# for i in range(5):  # range(5) generates numbers 0 to 4
#     print(i)

# # break and continue
# for num in range(2, 10):
#     if num % 2 == 0:
#         print(f"Found an even number {num}")
#         continue
#     print(f"Found an odd number {num}")

# for num in range(2, 10):
#     if num % 2 == 0:
#         print(f"Found an even number {num}")
#         break
#     print(f"Found an odd number {num}")


# Match
command = "start"
match command:
    case "start":
        print("Starting the program...")
    case "stop":
        print("Stopping the program...")
    case "pause":
        print("Pausing the program...")
    case _:
        print("Unknown command.")
