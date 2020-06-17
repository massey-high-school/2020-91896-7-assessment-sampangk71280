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
    valid = False
    while not valid:
        response = input("Do you want to calculate the area, perimeter, or both?")

        if response == "area" or response == "perimeter" or response == "both":
            return response
        else:
            print("Please input a valid response!")

def circle(ask):
    radius = intcheck("Radius: ")
    area = math.pi * radius ** 2
    perimeter = 2 * math.pi * radius

    return area, perimeter

def square(ask):
    length = intcheck("Length: ")
    area = length * length
    perimeter =  length * 4

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

    if shape == "square":
        response = area_or_perimeter()
        length = square(response)

        if response == "area":
            print("-----{}-----\nArea: {:.2f}\n".format(shape, length[0]))
        elif response == "perimeter":
            print("-----{}-----\nArea: {:.2f}\n".format(shape, length[1]))
        elif response == "both":
            print("-----{}-----\nArea: {:.2f}\nPerimeter: {:.2f}".format(shape, length[0], length[1]))
        else:
            print("Error")



