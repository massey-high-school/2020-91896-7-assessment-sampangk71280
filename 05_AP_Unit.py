# Area Perimeter - Component 5

# To do:
# Ask user what unit they want to use

# Functions

# recycled not blank function
def unit_checker(question, error_msg, num_ok):
    error = error_msg #error message
    valid = False
    while not valid:
        unit = input(question)
        has_errors = ""


        if num_ok !="yes":
            #  look at each character in string and if it's a number, complain
            for letter in unit:
                if letter.isdigit() == True:
                    has_errors = "yes"
                    break

        if unit == "":
            # prints error when left blank
            print(error)
            continue
        elif has_errors != "": # prints errors when there is a number (if num_ok is no)
            print(error)
            continue
        else:
            return unit


length = 2
shape = "Square"
area = 2
perimeter = 8
unit = unit_checker("What units are you using for your calculation?", "Please enter units and do not leave it blank!!", "no")
print("-----{}-----\nArea: {}{}\nPerimeter: {}{}".format(shape, area, unit, perimeter,unit))