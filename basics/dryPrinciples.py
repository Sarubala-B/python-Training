# ❌ Repeating the same logic in multiple places
def calculate_area_circle(radius):
    return 3.1415 * radius * radius

def calculate_area_square(side):
    return side * side

def calculate_area_rectangle(length, width):
    return length * width


# ✅ Using a reusable function
def calculate_area(shape, *dimensions):
    shapes = {
        "circle": lambda r: 3.1415 * r * r,
        "square": lambda s: s * s,
        "rectangle": lambda l, w: l * w
    }
    return shapes.get(shape, lambda: "Invalid shape")(*dimensions)

print(calculate_area("circle", 5))  
print(calculate_area("square", 4))   
print(calculate_area("rectangle", 4, 6)) 
