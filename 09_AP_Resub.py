# Area Perimeter - Component 8 Usability

# Used for pi
import math

# **** Functions ****

# String Checker
# Checks that the user's input is in list
def string_checker(question, error, options):
    valid = False
    while not valid:
        # question
        response = input(question).lower()

        # returns valid response if it's in list
        if response in options:
            return response
        # prints error message
        else:
            print(error)

# Number checking function
# Recycled from previous program and edited to fit
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

# Gets radius for circle and calculates area and perimeter
def circle(ask):
    radius = intcheck("What is the radius?\nRadius: ")
    # Formulas for area and perimeter
    area = math.pi * radius ** 2
    perimeter = 2 * math.pi * radius
    return area, perimeter

# Gets length and width for square and rectangle and calculates area and perimeter
def square_rectangle(ask):
    length = intcheck("What is the length?\nLength: ")
    width = length # For squares, all sides are the same
    # Gets width for rectangle
    if shape == "rectangle" or shape == "r":
        width = intcheck ("What is the width?\nWidth: ")
    # Formulas for area and perimeter
    area = length * width
    perimeter = (2 * length) + (2 * width)
    return area, perimeter

# Gets dimensions for triangle and calculates area and perimeter
def triangle(ask):
    # Gets base and height, only calculates area
    if ask == "area" or ask == "a":
        base = intcheck("What is the base?\nBase: ")
        height = intcheck("What is the height?\nHeight: ")
        area = 0.5 * base * height
        perimeter = "n/a"
    # Gets three sides, only calculates perimeter
    elif ask == "perimeter" or ask == "p":
        side_a = intcheck("How long is Side A?\nSide A: ")
        side_b = intcheck("How long is Side B?\nSide B: ")
        side_c = intcheck("How long is Side C?\nSide C: ")
        area = "n/a"
        perimeter = side_a + side_b + side_c
    # Gets all dimensions and calculates area and perimeter
    elif ask == "both" or ask == "b":
        base = intcheck("What is the base?\nBase:  ") # Base is equivalent to one of the sides so only two sides are needed
        height = intcheck("What is the height?\nHeight: ")
        area = 0.5 * base * height
        side_a = intcheck("How long is Side A?\nSide A: ")
        side_b = intcheck("How long is Side B?\nSide B: ")
        perimeter = side_a + side_b + base
    return area, perimeter

# Gets dimensions for parallelogram, calculates area and perimeter
def parallelogram(ask):
    # Gets base and height, only calculates area
    if ask == "area" or ask == "a":
        base = intcheck("What is the base?\nBase: ")
        height = intcheck("What is the height?\nHeight: ")
        area = base * height
        perimeter = "n/a"
    # Gets three sides, only calculates perimeter
    elif ask == "perimeter" or ask == "p":
        side_a = intcheck("How long is Side A?\nSide A: ")
        side_b = intcheck("How long is Side B?\nSide B: ")
        area = "n/a"
        perimeter = 2 * (side_a + side_b)
    elif ask == "both" or  ask == "b":
    # Gets all dimensions and calculates area and perimter
        base = intcheck("What is the base?\nBase:  ")
        height = intcheck("What is the height?\nHeight: ")
        area = base * height
        side_a = intcheck("How long is Side A?\nSide A: ")
        perimeter = 2 * (side_a + base)
    return area, perimeter

# Gets dimensions for trapezium, calculates area and perimeter
def trapzeium(ask):
    # Gets height and two sides, only calculates area
    if ask == "area" or ask == "a":
        height = intcheck("What is the height?\nHeight: ")
        side_a = intcheck("How long is Side A?\nSide A:  ")
        side_b = intcheck("How long is Side B?\nSide B:  ")
        area = (side_a + side_b)/2 * height
        perimeter = "n/a"
    elif ask == "perimeter" or ask == "p":
    # Gets all sides, only calculates perimeter
        side_a = intcheck("How long is Side A?\nSide A: ")
        side_b = intcheck("How long is Side B?\nSide B: ")
        side_c = intcheck("How long is Side C?\nSide C: ")
        side_d = intcheck("How long is Side D?\nSide D:  ")
        area = "n/a"
        perimeter = side_a + side_b + side_c + side_d
    elif ask == "both" or ask == "b":
    # Gets all dimensions, calculates height and perimeter
        height = intcheck("What is the height?\nHeight: ")
        side_a = intcheck("How long is Side A?\nSide A:  ")
        side_b = intcheck("How long is Side B?\nSide B:   ")
        area = (side_a + side_b) / 2 * height
        side_c = intcheck("How long is Side C?\nSide C: ")
        side_d = intcheck("How long is Side D?\nSide D:  ")
        perimeter = side_a + side_b + side_c + side_d
    return area, perimeter

# Recycled, checks that user inputs something
def not_blank(question, error_msg, num_ok):
    error = error_msg  # Error message
    valid = False
    while not valid:
        unit = input(question)
        has_errors = ""

        if num_ok != "yes":
            #  Look at each character in string and if it's a number, complain
            for letter in unit:
                if letter.isdigit() == True:
                    has_errors = "yes"
                    break

        if unit == "":
            # Prints error when left blank
            print(error)
            continue
        elif has_errors != "":  # Prints errors when there is a number (if num_ok is no)
            print(error)
            continue
        else:
            return unit


# Main Routine

history = [] # Master list
yes_no = ["yes", "y", "no", "n"] # Contains yes and no for instructions

# Asks user if they've used the calculator before
instructions = string_checker("Is this your first time using the Area/Perimeter Calculator?",
                              "Please choose 'y' or 'n'!", yes_no)

# For first timers, prints out instructions
if instructions == "yes" or instructions == "y":
    print("\nWELCOME TO AREA/PERIMETER CALCULATOR!\n"
          "- This calculator will automatically calculate the area and/or perimeter of a chosen shape.\n"
          "- The shapes available are: circle, square, rectangle, triangle, parallelogram, and trapezium.\n"
          "- It will ask you for dimensions and unit.\n"
          "- Don't forget to hit <enter> after each input!\n")
# Skips instructions for people who've used the calculator before
elif instructions == "no" or instructions == "n":
    print()

# Loops entire calculator
keep_going = ""
while keep_going == "":

    # Set to zero at the beginning and dimension will be added
    area = 0
    perimeter = 0

    shape_history = []  # Adds shape to list after each use
    # Shapes available
    possible_shapes = ["circle", "c", "square", "s", "rectangle", "r", "triangle", "tr", "parallelogram", "p", "trapezium", "tz"]
    # Two different ways for users to respond
    options = ["a", "area", "p", "perimeter", "b", "both"]

    # Asks user for shape
    shape = string_checker("Please choose a shape to pick from: circle (c), square (s), rectangle (r), triangle (tr), parallelogram (p), trapezium (tz)\n"
                           "Shape: ", "Ooops! Please choose one of the shapes in the list!\n", possible_shapes)

    # Asks user for unit, accepts any letters but not numbers/blank
    unit = not_blank("\nWhat units are you using for your calculation?",
                     "Please enter units, not numbers, do not leave it blank!", "no")

    # Asks user if they want to calculate area, perimeter, or both
    a_p = string_checker("\nDo you want to calculate the area (a), perimeter (p), or both (b)?", "Please choose a, p, or b!", options)
    print()

    # Calls different function for each shape
    # After getting the dimensions, shape is renamed back to full shape name (instead of abbreivation) to make printing out heading better
    if shape == "circle" or shape == "c":
        dimension = circle(a_p)
        shape = "circle"
    elif shape == "square" or shape == "s" or shape == "rectangle" or shape == "r":
        dimension = square_rectangle(a_p)
        if shape == "s":
            shape = "square"
        elif shape == "r":
            shape = "rectangle"
    elif shape == "triangle" or shape == "tr":
        dimension = triangle(a_p)
        shape = "triangle"
    elif shape == "parallelogram" or shape == "p":
        dimension = parallelogram(a_p)
        shape = "parallelogram"
    elif shape == "trapezium" or shape == "tz":
        dimension = trapzeium(a_p)
        shape = "trapezium"

    shape_history.append(shape)  # Puts shape in list

    # Adds measurement to area and/or perimeter
    if shape in possible_shapes:
        # User chooses area
        if a_p == "area" or a_p == "a":
            area += dimension[0] # adds the measurement to area
            area = "{:.2f}".format(area) # rounds to 2 dp
            perimeter = "n/a" # perimeter is not calculated
        # User chooses perimeter
        elif a_p == "perimeter" or a_p == "p":
            perimeter += dimension[1] # adds the measurement to perimeter
            perimeter = "{:.2f}".format(perimeter) # rounds to 2dp
            area = "n/a" # area is not calculated
        # User chooses area and perimeter
        elif a_p == "both" or a_p == "b":
            area += dimension[0] # adds measurement to area
            area = "{:.2f}".format(area) # rounds to 2 dp
            perimeter += dimension[1] # adds measurement to perimeter
            perimeter = "{:.2f}".format(perimeter) # rounds to 2 dp

        # Prints out calculation
        print("\n-----{}-----\nArea: {} {}^2\nPerimeter: {} {}\n".format(shape.capitalize(), area, unit, perimeter, unit)) # .capitalize() makes the first letter uppercase

        shape_history.append(area) # adds area measurement to shape history
        shape_history.append(perimeter) # adds perimeter measure to shape history
        shape_history.append(unit) # adds unit to shape history

    history.append(shape_history) # adds shape_history to master history list (list within a list)

    # Asks user if they want to continue using calculator
    keep_going = input("Do you want to continue using the calculator? Press <enter> for yes and any key for no") # loops if nothing is entered
    print()

print("**********HISTORY**********\n")
# Prints out calculation history
for item in history:
    print("-----{}-----\nArea:{} {}^2\nPerimeter:{} {}\n".format(item[0].capitalize(), item[1], item[3], item[2], item[3]))
