from shapes import *

# Create a list to hold shape instances
shapes = []

# Add two Rectangle objects
rect1 = Rectangle(10, 20, "Rectangle_1")
rect2 = Rectangle(20, 30, "Rectangle_2")
shapes.append(rect1)
shapes.append(rect2)

# Add two Circle objects
circle1 = Circle(0, 0, 4, "Circle_1")
circle2 = Circle(5, 5, 9, "Circle_2")
shapes.append(circle1)
shapes.append(circle2)

# Add one Square object
square = Square(10, "Square")
shapes.append(square)

# Display polymorphism check
print("--- Polymorphism check ---")
for shape in shapes:
    print(f"{shape.name} Area = {shape.area:.5f}")

# Getter/setter check for Circle
print("\n--- Getter/setter check ---")
print(f"Circle_1 Current: {circle1.radius} {circle1.area:.5f}")
circle1.radius = 8
print(f"Circle_1 Doubled: {circle1.radius} {circle1.area:.5f}")

# Getter/setter check for Rectangle
print(f"\nRectangle_1 Current: {rect1.length} {rect1.width} {rect1.area}")
rect1.length = 15
rect1.width = 20
print(f"Rectangle_1 Modified: {rect1.length} {rect1.width} {rect1.area}")

# Getter/setter check for Square
print(f"\nSquare Current: {square.side} {square.area}")
square.side = 15
print(f"Square Modified: {square.side} {square.area}")

for shape in shapes:
    if isinstance(shape, Circle):
        print(f"{shape.name} is a Circle with radius {shape.radius}")
    elif isinstance(shape, Rectangle):
        print(f"{shape.name} is a Rectangle with length {shape.length} and width {shape.width}")
    elif isinstance(shape, Square):
        print(f"{shape.name} is a Square with side {shape.side}")
    print(f"{shape.name} Area = {shape.area:.5f}")