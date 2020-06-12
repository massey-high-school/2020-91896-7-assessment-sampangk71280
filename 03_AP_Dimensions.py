# Area Perimeter - Component 3

# To do:
# Get user's shape choice and find area and perimeter

# used for pi
import math

# functions
# Checks that the user choices a shape from the list
def shape_checker(question, error):
    valid = False
    while not valid:
        # question
        shape = input(question).lower()

        # continues if valid shape is chosen
        if shape in possible_shapes:
            return shape
        # prints error message
        else:
            print(error)

# Number checking function
# recycled from previous programs and edited
def intcheck(question, number):
    valid = False
    while not valid:
        # Error message
        error = "Whoops! Please enter a valid number above {}!".format(number)

        try:
            response = float(input(question))

            # Returns if response is bigger than number
            if number < response:
                return response
            # If response is less than number, print out error, and keep asking until valid input
            else:
                print(error)
                print()

        except ValueError:
            print(error)


# Shapes available
possible_shapes = ["circle", "square", "rectangle", "triangle", "parallelogram", "trapezium"]

# Code from https://www.edureka.co/community/1792/how-to-print-array-list-without-brackets-in-python
# .join removes brackets and ' when printing out the list and adds a space between each item
choices =(', ' .join(possible_shapes))

# asks user for shape
shape = shape_checker("Please choose a shape to pick from: {} \nShape: ".format(choices), "Oops please choose a shape from the list!")

# user chooses circle
if shape == "circle":
    # gets radius
    radius = intcheck("Radius: ", 0)
    # calculates area and perimeter
    circle_area = math.pi * radius ** 2
    circle_perimeter = 2 * math.pi * radius
    print("-----Circle----- \nArea: {:.2f}\nPerimeter: {:.2f}\n".format(circle_area, circle_perimeter))

# user chooses square
elif shape == "square":
    # gets length
    length = intcheck("Length: ", 0)
    # calculates area and perimeter
    square_area = length * length
    square_perimeter = length * 4
    print("-----Square-----\nArea: {:.2f}\nPerimeter: {:.2f}\n".format(square_area, square_perimeter))

# user chooses rectangle
elif shape == "rectangle":
    # gets length and width
    length = intcheck("Length: ", 0)
    width = intcheck("Width: ", 0)
    # calculates area and perimeter
    rectangle_area = length * width
    rectangle_perimeter = (2 * length) + (2 * width)
    print("-----Rectangle-----\nArea: {:.2f}\nPerimeter: {:.2f}\n".format(rectangle_area, rectangle_perimeter))

# user chooses triangle
elif shape == "triangle":
    # gets base, height, and sides
    base = intcheck("Base: ", 0)
    height = intcheck("Height: ", 0)
    side_a = intcheck("Side A: ", 0)
    side_b = intcheck("Side B: ", 0)
    side_c = intcheck("Side C: ", 0)
    # calculates area and perimeter
    triangle_area = 0.5 * base * height
    triangle_perimeter = side_a + side_b + side_c
    print("-----Triangle-----\nArea: {:.2f}\nPerimeter: {:.2f}\n".format(triangle_area, triangle_perimeter))

# user chooses parallelogram
elif shape == "parallelogram":
    # gets base, height, and sides
    base = intcheck("Base: ", 0)
    height = intcheck("Height: ", 0)
    side_a = intcheck("Side A: ", 0)
    side_b = intcheck("Side B: ", 0)
    # calculates area and perimeter
    parallelogram_area = base * height
    parallolgram_perimeter = 2 * (side_a + side_b)
    print("-----Parallelogram-----\nArea: {:.2f}\nPerimeter: {:.2f}\n".format(parallelogram_area, parallolgram_perimeter))

# user chooses trapezium
elif shape == "trapezium":
    # gets height and sides
    height = intcheck("Height: ", 0)
    side_a = intcheck("Side A: ", 0)
    side_b = intcheck("Side B: ", 0)
    side_c = intcheck("Side C: ", 0)
    side_d = intcheck("Side D: ", 0)
    # calculates area and perimeter
    trapezium_area = (side_a + side_b) / 2 * height
    trapezium_perimeter = side_a + side_b + side_c + side_d
    print("-----Trapezium-----\nArea: {:.2f}\nPerimeter: {:.2f}\n".format(trapezium_area, trapezium_perimeter))

else:
    print("errrorrr")






