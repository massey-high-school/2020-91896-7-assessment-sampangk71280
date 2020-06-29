# Area Perimeter - Component 6

# To do:
# put shapes into a shape list
# put measurements into a list
# put shapes and measurements into one master list
# print out master list

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

    if ask == "area":
        return area
    elif ask == "perimeter":
        return perimeter
    elif ask == "both":
        return area, perimeter

def triangle(ask):
    # gets base and height, only calculates area
    if ask == "area" or ask == "a":
        base = intcheck("Base: ")
        height = intcheck("Height: ")
        area = 0.5 * base * height
        return area
    # gets three sides, only calculates perimeter
    elif ask == "perimeter" or ask == "p":
        side_a = intcheck("Side A:")
        side_b = intcheck("Side B:")
        side_c = intcheck("Side C:")
        perimeter = side_a + side_b + side_c
        return perimeter
    # gets all dimensions and calculates area and perimeter
    elif ask == "both" or ask == "b":
        base = intcheck("Base: ")
        height = intcheck("Height: ")
        area = 0.5 * base * height
        side_a = intcheck("Side A:")
        side_b = intcheck("Side B:")
        side_c = intcheck("Side C:")
        perimeter = side_a + side_b + side_c
        return area, perimeter

def parallelogram(ask):
    # gets base and height, only calculates area
    if ask == "area" or ask == "a":
        base = intcheck("Base: ")
        height = intcheck("Height: ")
        area = base * height
        return area
    # gets three sides, only calculates perimeter
    elif ask == "perimeter" or ask == "p":
        side_a = intcheck("Side A:")
        side_b = intcheck("Side B:")
        perimeter = 2 * (side_a + side_b)
        return perimeter
    elif ask == "both" or  ask == "b":
    # gets all dimensions and calculates area and perimter
        base = intcheck("Base: ")
        height = intcheck("Height: ")
        area = base * height
        side_a = intcheck("Side A:")
        side_b = intcheck("Side B:")
        perimeter = 2 * (side_a + side_b)
        return area, perimeter

def trapzeium(ask):
    # gets height and two sides, only calculates area
    if ask == "area" or ask == "a":
        height = intcheck("Height: ")
        side_a = intcheck("Side A: ")
        side_b = intcheck("Side B: ")
        area = (side_a + side_b)/2 * height
        return area
    elif ask == "perimeter" or ask == "p":
    # gets all sides, only calculates perimeter
        side_a = intcheck("Side A:")
        side_b = intcheck("Side B:")
        side_c = intcheck("Side C:")
        side_d = intcheck("Side D: ")
        perimeter = side_a + side_b + side_c + side_d
        return perimeter
    elif ask == "both" or ask == "b":
    # gets all dimensions, calculates height and perimeter
        height = intcheck("Height: ")
        side_a = intcheck("Side A: ")
        side_b = intcheck("Side B: ")
        area = (side_a + side_b) / 2 * height
        side_c = intcheck("Side C:")
        side_d = intcheck("Side D: ")
        perimeter = side_a + side_b + side_c + side_d
        return area, perimeter

def not_blank(question, error_msg, num_ok):
    error = error_msg  # error message
    valid = False
    while not valid:
        unit = input(question)
        has_errors = ""

        if num_ok != "yes":
            #  look at each character in string and if it's a number, complain
            for letter in unit:
                if letter.isdigit() == True:
                    has_errors = "yes"
                    break

        if unit == "":
            # prints error when left blank
            print(error)
            continue
        elif has_errors != "":  # prints errors when there is a number (if num_ok is no)
            print(error)
            continue
        else:
            return unit

history = [] # master list
shape_history = [] # shape history
measure_history = [] # contains all measurements

# Main Routine
# Loops entire calculator
keep_going = ""
while keep_going == "":

    # Shapes available
    possible_shapes = ["circle", "square", "rectangle", "triangle", "parallelogram", "trapezium"]

    # Code from https://www.edureka.co/community/1792/how-to-print-array-list-without-brackets-in-python
    # .join removes brackets and ' when printing out the list and adds a space between each item
    choices =(', ' .join(possible_shapes))

    # asks user for shape
    shape = shape_checker("Please choose a shape to pick from: {} \nShape: ".format(choices), "Oops please choose a shape from the list!")
    # asks user for unit, accepts any letters but not numbers/blank
    unit = not_blank("What units are you using for your calculation?",
                     "Please enter units, not numbers, do not leave it blank!", "no")

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

    #print(dimension[0])

    if shape in possible_shapes:
        if response == "area" or response == "a":
            print("-----{}-----\nArea: {:.2f}{}^2\n".format(shape, dimension, unit))
        elif response == "perimeter" or response == "p":
            print("-----{}-----\nPerimeter: {:.2f}{}\n".format(shape, dimension, unit))
        elif response == "both" or response == "b":
            print("-----{}-----\nArea: {:.2f}{}^2\nPerimeter: {:.2f}{}\n".format(shape, dimension[0], unit, dimension[1] ,unit))

    keep_going = input("Do you want to continue using the calculator? Press <enter> for yes and any key for no")
    print()





