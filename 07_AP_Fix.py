# Area Perimeter - Component 7

# To do:
# fix inefficient code
# string checker for both shape and AP
# all square are rectangle
# just return both area and perimeter for circle, square, and rectangle
# triangle function slightly inefficient
# print out n/a if user doesn't choose both

# used for pi
import math

# functions
# Checks that the user choices a shape from the list
def string_checker(question, error):
    valid = False
    while not valid:
        # question
        response = input(question).lower()

        # returns valid response if it's in list
        if response in possible_shapes:
            return response
        elif response in options:
            return response
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

# gets radius for circle and calculates area and perimeter
def circle(ask):
    radius = intcheck("Radius: ")
    #formulas for area and perimeter
    area = math.pi * radius ** 2
    perimeter = 2 * math.pi * radius
    return area, perimeter

# gets length and width for square and rectangle and calculates area and perimter
def square_rectangle(ask):
    length = intcheck("Length: ")
    width = length
    if shape == "rectangle":
        width = intcheck ("Width: ")
        #formulas for area and perimeter
    area = length * width
    perimeter = (2 * length) + (2 * width)
    return area, perimeter

# gets dimensions for triangle and calculates area and perimeter
def triangle(ask):
    # gets base and height, only calculates area
    if ask == "area" or ask == "a":
        base = intcheck("Base: ")
        height = intcheck("Height: ")
        area = 0.5 * base * height
        perimeter = "n/a"
    # gets three sides, only calculates perimeter
    elif ask == "perimeter" or ask == "p":
        side_a = intcheck("Side A:")
        side_b = intcheck("Side B:")
        side_c = intcheck("Side C:")
        area = "n/a"
        perimeter = side_a + side_b + side_c
    # gets all dimensions and calculates area and perimeter
    elif ask == "both" or ask == "b":
        base = intcheck("Base: ")
        height = intcheck("Height: ")
        area = 0.5 * base * height
        side_a = intcheck("Side A:")
        side_b = intcheck("Side B:")
        perimeter = side_a + side_b + base
    return area, perimeter

# gets dimensions for parallelogram, calculates area and perimeter
def parallelogram(ask):
    # gets base and height, only calculates area
    if ask == "area" or ask == "a":
        base = intcheck("Base: ")
        height = intcheck("Height: ")
        area = base * height
        perimeter = "n/a"
    # gets three sides, only calculates perimeter
    elif ask == "perimeter" or ask == "p":
        side_a = intcheck("Side A:")
        side_b = intcheck("Side B:")
        area = "n/a"
        perimeter = 2 * (side_a + side_b)
    elif ask == "both" or  ask == "b":
    # gets all dimensions and calculates area and perimter
        base = intcheck("Base: ")
        height = intcheck("Height: ")
        area = base * height
        side_a = intcheck("Side A:")
        side_b = intcheck("Side B:")
        perimeter = 2 * (side_a + side_b)
    return area, perimeter

# gets dimensions for trapezium, calculates area and perimeter
def trapzeium(ask):
    # gets height and two sides, only calculates area
    if ask == "area" or ask == "a":
        height = intcheck("Height: ")
        side_a = intcheck("Side A: ")
        side_b = intcheck("Side B: ")
        area = (side_a + side_b)/2 * height
        perimeter = ""
    elif ask == "perimeter" or ask == "p":
    # gets all sides, only calculates perimeter
        side_a = intcheck("Side A:")
        side_b = intcheck("Side B:")
        side_c = intcheck("Side C:")
        side_d = intcheck("Side D: ")
        area = ""
        perimeter = side_a + side_b + side_c + side_d
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

# recycled, checks that user inputs something
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


# Main Routine
history = [] # master list
# Loops entire calculator
keep_going = ""
while keep_going == "":

    # set to zero at the beginning and dimension will be added
    area = 0
    perimeter = 0

    shape_history = []  # shape history
    # Shapes available
    possible_shapes = ["circle", "square", "rectangle", "triangle", "parallelogram", "trapezium"]
    # two different ways for users to respond
    options = ["a", "area", "p", "perimeter", "b", "both"]

    # Code from https://www.edureka.co/community/1792/how-to-print-array-list-without-brackets-in-python
    # .join removes brackets and ' when printing out the list and adds a space between each item
    choices =(', ' .join(possible_shapes))

    # asks user for shape
    shape = string_checker("Please choose a shape to pick from: {} \nShape: ".format(choices), "Oops please choose a shape from the list!")
    shape_history.append(shape) # puts shape in list
    # asks user for unit, accepts any letters but not numbers/blank
    unit = not_blank("What units are you using for your calculation?",
                     "Please enter units, not numbers, do not leave it blank!", "no")
    # asks user if they want to calculate area, perimeter, or both
    a_p = string_checker("Do you want to calculate the area (a), perimeter (p), or both (b)?", "Please choose a, p, or b!")

    # calls different function for each shape
    if shape == "circle":
        dimension = circle(a_p)
    elif shape == "square" or shape == "rectangle":
        dimension = square_rectangle(a_p)
    elif shape == "triangle":
        dimension = triangle(a_p)
    elif shape == "parallelogram":
        dimension = parallelogram(a_p)
    elif shape == "trapezium":
        dimension = trapzeium(a_p)

    # adds measurement to area and/or perimeter
    if shape in possible_shapes:
        if a_p == "area" or a_p == "a":
            area += dimension[0]
            area = "{:.2f}".format(area)
            perimeter = "n/a"
        elif a_p == "perimeter" or a_p == "p":
            perimeter += dimension[1]
            perimeter = "{:.2f}".format(perimeter)
            area = "n/a"

        elif a_p == "both" or a_p == "b":
            area += dimension[0]
            perimeter += dimension[1]

        # prints out calculation
        print("-----{}-----\nArea: {} {}^2\nPerimeter: {} {}\n".format(shape.capitalize(), area, unit, perimeter, unit)) # .capitalize() makes the first letter uppercase
        shape_history.append(area) # adds area measurement to shape history
        shape_history.append(perimeter) # adds perimeter measure to shape history
        shape_history.append(unit) # adds unit to shape history

    history.append(shape_history) # adds shape_history to master history list (list within a list)

    # asks user if they want to continue using calculator
    keep_going = input("Do you want to continue using the calculator? Press <enter> for yes and any key for no")
    print()

print("*****HISTORY*****")
# prints out calculation history
for item in history:
    print("-----{}-----\nArea:{} {}^2\nPerimeter:{} {}\n".format(item[0].capitalize(), item[1], item[3], item[2], item[3]))
