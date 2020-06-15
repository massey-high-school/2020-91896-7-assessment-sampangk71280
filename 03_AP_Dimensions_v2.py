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


def dimensions_needed(shape, length_type):
    length_type = ["length", "width", "base", "height", "side_a", "side_b", "side_c", "side_d"]

    length = intcheck("Length: ", 0)
    width = intcheck("Width: ", 0)
    base = intcheck("Base: ", 0)
    height = intcheck("Height: ", 0)
    side_a = intcheck("Side A: ", 0)
    side_b = intcheck("Side B: ", 0)
    side_c = intcheck("Side C: ", 0)
    side_d = intcheck("Side D: ", 0)

# set lengths to zero until needed
radius = 0
length = 0
width = 0
base = 0
height = 0
side_a = 0
side_b = 0
side_c = 0
side_d = 0

# Formula list
# circles
circle_area = math.pi * radius**2
circle_perimeter = 2 * math.pi * radius
# squares
square_area = length * 2
square_perimeter = length * 4
# rectangles
rectangle_area = length * width
rectangle_perimeter = (2 * length) + (2 * width)
# triangle
triangle_area = 0.5 * base * height
triangle_perimeter = side_a + side_b +side_c
# parallelogram
parallelogram_area = base * height
parallolgram_perimeter = 2 * (side_a + side_b)
# trapezium
trapezium_area = (side_a + side_b)/2 * height
trapezium_perimeter = side_a + side_b + side_c + side_d


# Shapes available
possible_shapes = ["circle", "square", "rectangle", "triangle", "parallelogram", "trapezium"]

# Code from https://www.edureka.co/community/1792/how-to-print-array-list-without-brackets-in-python
# .join removes brackets and ' when printing out the list and adds a space between each item
choices =(', ' .join(possible_shapes))

# asks user for shape
shape = shape_checker("Please choose a shape to pick from: {} \nShape: ".format(choices), "Oops please choose a shape from the list!")





