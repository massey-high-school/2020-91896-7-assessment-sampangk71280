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


def dimensions_needed(shape):
    if shape == "circle":
        # gets radius
        radius = intcheck("Radius: ")
        # calculates area and perimeter
        area = math.pi * radius ** 2
        perimeter = 2 * math.pi * radius

    elif shape == "square" or shape == "rectangle":
        # gets length
        length = intcheck("Length: ")
        # calculates area and perimeter of a square
        area = length * length
        perimeter = length * 4
        if shape == "rectangle":
            # gets width
            width = intcheck("Width: ")
            # calculates area and perimeter of a rectangle
            area = length * width
            perimeter = (2 * length) + (2 * width)

    elif shape == "triangle" or shape == "parallelogram" or shape == "trapezium":
        # gets height
        height = intcheck("Height: ")
        side_a = intcheck("Side A: ")
        side_b = intcheck("Side B: ")
        if shape == "parallelogram" or shape == "triangle":
            base = intcheck("Base: ")
        elif shape == "triangle" or "trapezium":
            side_c = intcheck("Side C: ")
        elif shape == "trapezium":
            side_d = intcheck("Side D: ", 0)

    # formats statements 
    print("-----{}-----\nArea: {:.2f}\nPerimeter: {:.2f}\n".format(shape,area,perimeter))
    return area, perimeter



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
    dimensions = dimensions_needed(shape)
    # print(dimensions)





