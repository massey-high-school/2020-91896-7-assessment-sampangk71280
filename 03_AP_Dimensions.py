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
            break
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
# choices =(', ' .join(possible_shapes))

# asks user for shape
shape = shape_checker("Please choose a shape to pick from: {} \nShape: ".format(possible_shapes), "Oops please choose a shape from the list!")

if shape == "circle":
    radius = int("Radius")
else:
    print("errrorrr")

    """"circle_area = math.pi * radius ** 2
    circle_perimeter = 2 * math.pi * radius
    print("Circle \nArea: {:.2f}\nPerimeter: {:.2f}\n".format(circle_area, circle_perimeter))"""""




