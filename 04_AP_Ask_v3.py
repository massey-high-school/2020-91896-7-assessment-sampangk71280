

# Area Perimeter - Component 4

# To do:
# make a function for each shape

# Functions

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

def area_or_perimeter():
    options = ["a", "area", "p", "perimeter", "b", "both"]
    valid = False
    while not valid:
        response = input("Do you want to calculate the area (a), perimeter (p), or both (b)?").lower()

        if response in options:
            return response
        else:
            print("Please input a valid response!")

# gets radius for circle and calculates area and perimeter
def circle(ask):
    radius = intcheck("Radius: ")
    #formulas for area and perimeter
    area = math.pi * radius ** 2
    perimeter = 2 * math.pi * radius
    return area, perimeter

# gets length for square and calculate area and perimeter
def square(ask):
    length = intcheck("Length: ")
    # formulas for area and perimeter
    area = length * length
    perimeter =  length * 4
    return area, perimeter

# gets length and width for rectangle and calculates area and perimter
def rectangle(ask):
    length = intcheck("Length: ")
    width = intcheck ("Width: ")
    #formulas for area and perimeter
    area = length * width
    perimeter = (2 * length) + (2 * width)

    return area, perimeter

def triangle(ask):
    # gets base and height, only calculates area
    if ask == "area":
        base = intcheck("Base: ")
        height = intcheck("Height: ")
        area = 0.5 * base * height
        return area
    # gets three sides, only calculates perimeter
    elif ask == "perimeter":
        side_a = intcheck("Side A:")
        side_b = intcheck("Side B:")
        side_c = intcheck("Side C:")
        perimeter = side_a + side_b + side_c
        return perimeter
    # gets all dimensions and calculates area and perimeter
    elif ask == "both":
        base = intcheck("Base: ")
        height = intcheck("Height: ")
        area = 0.5 * base * height
        side_a = intcheck("Side A:")
        side_b = intcheck("Side B:")
        side_c = intcheck("Side C:")
        perimeter = side_a + side_b + side_c
        return area, perimeter

def parallelogram(ask):
    if ask == "area":
        base = intcheck("Base: ")
        height = intcheck("Height: ")
        area = base * height
        return area
    elif ask == "perimeter":
        side_a = intcheck("Side A:")
        side_b = intcheck("Side B:")
        perimeter = 2 * (side_a + side_b)
        return perimeter
    elif ask == "both":
        base = intcheck("Base: ")
        height = intcheck("Height: ")
        area = base * height
        side_a = intcheck("Side A:")
        side_b = intcheck("Side B:")
        perimeter = 2 * (side_a + side_b)
        return area, perimeter

def trapzeium(ask):
    if ask == "area" or ask == "both":
        height = intcheck("Height: ")
        side_a = intcheck("Side A: ")
        side_b = intcheck("Side B: ")
        area = (side_a + side_b)/2 * height
        return area
    elif ask == "perimeter":
        side_a = intcheck("Side A:")
        side_b = intcheck("Side B:")
        side_c = intcheck("Side C:")
        side_d = intcheck("Side D: ")
        perimeter = side_a + side_b + side_c + side_d
        return perimeter
    elif ask == "both":
        height = intcheck("Height: ")
        side_a = intcheck("Side A: ")
        side_b = intcheck("Side B: ")
        area = (side_a + side_b) / 2 * height
        side_c = intcheck("Side C:")
        side_d = intcheck("Side D: ")
        perimeter = side_a + side_b + side_c + side_d
        return area, perimeter

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

    # asks user if they want to calculate area, perimeter, or both
    response = area_or_perimeter().lower()

    if shape == "circle":
        dimension = circle(response)
    elif shape == "square":
        dimension = square(response)
    elif shape == "rectangle":
        dimension = rectangle(response)
    elif shape == "triangle":
        dimension = triangle(response)
    elif shape == "parallelogram":
        dimension = parallelogram(response)
    elif shape == "trapezium":
        dimension = trapzeium(response)

    if shape in possible_shapes:
        if response == "area" or response == "a":
            print("-----{}-----\nArea: {:.2f}\n".format(shape, dimension[0]))
        elif response == "perimeter" or response == "p":
            print("-----{}-----\nPerimeter: {:.2f}\n".format(shape, dimension[1]))
        elif response == "both" or response == "b":
            print("-----{}-----\nArea: {:.2f}\nPerimeter: {:.2f}".format(shape, dimension[0], dimension[1]))



