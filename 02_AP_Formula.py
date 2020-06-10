# Area Perimeter - Component 2

# To do:
# Get formulas for the area and perimeter for each shape

# used for pi
import math

# dimensions
radius = 3
length = 2
width = 4
base = 2.5
height = 5
side_a = 1
side_b = 2
side_c = 3
side_d = 4

# Circle formula
circle_area = math.pi * radius**2
circle_perimeter = 2 * math.pi * radius
print("Circle \nArea: {:.2f}\nPerimeter: {:.2f}\n".format(circle_area, circle_perimeter))

# Square formula
square_area = length * 2
square_perimeter = length * 4
print("Square\nArea: {:.2f}\nPerimeter: {:.2f}\n".format(square_area, square_perimeter))

# Rectangle formula
rectangle_area = length * width
rectangle_perimeter = (2 * length) + (2 * width)
print("Rectangle\nArea: {:.2f}\nPerimeter: {:.2f}\n".format(rectangle_area, rectangle_perimeter))

# Triangle formula
triangle_area = 0.5 * base * height
triangle_perimeter = side_a + side_b +side_c
print("Triangle\nArea: {:.2f}\nPerimeter: {:.2f}\n".format(triangle_area, triangle_perimeter))

# Parallelogram
parallelogram_area = base * height
parallolgram_perimeter = 2 * (side_a + side_b)
print("Parallelogram\nArea: {:.2f}\nPerimeter: {:.2f}\n".format(parallelogram_area, parallolgram_perimeter))

# Trapezium
trapezium_area = (side_a + side_b)/2 * height
trapezium_perimeter = side_a + side_b + side_c + side_d
print("Trapezium\nArea: {:.2f}\nPerimeter: {:.2f}\n".format(trapezium_area, trapezium_perimeter))