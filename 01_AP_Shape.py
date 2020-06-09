# Area Perimeter - Component 1

# To do:
# Ask user what shape they want to calculate

# Functions

# Checks that the user choices a shape from the list
def shape_checker(question, error):
    valid = False
    while not valid:
        # question
        shape = input(question).lower()

        # continues if valid shape is chosen
        if shape in possible_shapes:
            print("Good job!")
            break
        # prints error message
        else:
            print(error)


# Shapes available
possible_shapes = ["circle", "square", "rectangle", "triangle", "parallelogram", "trapezium"]

# Code from https://www.edureka.co/community/1792/how-to-print-array-list-without-brackets-in-python
# .join removes brackets and ' when printing out the list and adds a space between each item
choices =(', ' .join(possible_shapes))

# asks user for shape
for item in possible_shapes:
    shape = shape_checker("Please choose a shape to pick from: {} \nShape: ".format(choices), "Oops please choose a shape from the list!")

