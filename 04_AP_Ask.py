# Area Perimeter - Component

# To do:
# Create two functions to ask if they want to calculate area or perimeter


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
def intcheck(question):
    valid = False
    while not valid:
        number = 0
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

# calculates the area
def calculate_area(shape):
    if shape == "circle":
        radius = intcheck("Radius: ") # only circle needs radius
        area = math.pi * radius ** 2 # area of a circle

    elif shape == "square" or shape == "rectangle":
        length = intcheck("Length: ") # both square and rectangle needs length for area
        area = length * length # area of a square
        if shape == "rectangle":
            width = intcheck("Width: ") # only rectangle needs width for area
            area = length * width # area of a rectangle

    elif shape == "triangle" or shape == "parallelogram":
        # both triangle and parallelogram need base and height for area
        base = intcheck("Base: ")
        height = intcheck("Height: ")
        if shape == "triangle":
            area = 0.5 * base * height # area of triangle
        if shape == "parallelogram":
            area = base * height # area of parallelogram

    elif shape == "trapezium":
        side_a = intcheck("Side A: ")
        side_b = intcheck("Side B: ")
        height = intcheck("Height: ")
        area = (side_a + side_b) / 2 * height # area of trapezium

    return area

def calculate_perimeter(shape):

    if shape == "circle":
        radius = intcheck("Radius: ")
        perimeter = 2 * math.pi * radius

    elif shape == "square" or shape == "rectangle":
        length = intcheck("Length: ")
        perimeter = length * 4
        if shape == "rectangle":
            width = intcheck("Width: ")
            perimeter = (2 * length) + (2 * width)

    elif shape == "triangle" or shape == "parallelogram" or shape == "trapezium":
        side_a = intcheck("Side A: ")
        side_b = intcheck("Side B: ")
        perimeter = 2 * (side_a + side_b)
        if shape == "triangle":
            side_c = intcheck("Side C: ")
            perimeter = side_a + side_b + side_c
        elif shape == "trapezium":
            side_c = intcheck("Side C: ")
            side_d = intcheck("Side D: ")
            perimeter =side_a + side_b + side_c + side_d

    return perimeter

# Main Routine
# Loops entire calculator
keep_going = ""
while keep_going == "":

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

    # Shapes available
    possible_shapes = ["circle", "square", "rectangle", "triangle", "parallelogram", "trapezium"]

    # Code from https://www.edureka.co/community/1792/how-to-print-array-list-without-brackets-in-python
    # .join removes brackets and ' when printing out the list and adds a space between each item
    choices =(', ' .join(possible_shapes))

    # asks user for shape
    shape = shape_checker("Please choose a shape to pick from: {} \nShape: ".format(choices), "Oops please choose a shape from the list!")
    area_or_perimeter = input("Do you want to calculate area, perimeter or both?").lower()


    if area_or_perimeter == "area":
        area = calculate_area(shape)
        print("-----{}-----\nArea: {:.2f}\n".format(shape, area))
    elif area_or_perimeter == "perimeter":
        perimeter = calculate_perimeter(shape)
        print("-----{}-----\nPerimeter {:.2f}\n".format(shape, perimeter))
    elif area_or_perimeter == "both":
        area = calculate_area(shape)
        perimeter = calculate_perimeter(shape)
        print("-----{}-----\nArea: {:.2f}\nPerimeter: {:.2f}\n".format(shape, area, perimeter))
    else:
        print("Please choose!")




