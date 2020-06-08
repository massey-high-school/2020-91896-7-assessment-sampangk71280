# Area Perimeter - Component 1

# To do:
# Ask user what shape they want to calculate

# shapes available
possible_shapes = ["circle", "square", "rectangle", "triangle", "parallelogram", "trapezium"]
# asks user for shape wanted
shape = input("Please choose a shape to pick from: {}".format(possible_shapes)).lower()

# checks if user enters valid shape
if shape in possible_shapes:
    print("Yay")
else:
    print("oopsie")
