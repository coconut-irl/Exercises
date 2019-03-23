# Rewrite the area2.py program from the Examples above to have a 
# separate function for the area of a square, the area of a rectangle,
#  and the area of a circle (3.14 * radius**2).
#  This program should include a menu interface.


def hello():
    print("Hello!")

def print_welcome(name):
    print("Welcome, ", name)

def print_options():
    print()
    print("Options:")
    print(" 'p' Print options")
    print(" 'r' Calculate area of a rectangle")
    print(" 's' Calculate area of a square")
    print(" 'c' Calculate area of a circle")
    print(" 'q' Quit the program")
    print()

def positive_input(prompt):
    number = float(input(prompt))
    while number <= 0:
        print("Must be a positive number")
        number = float(input(prompt))
    return number

def rectangle_area(width, height):
    return width * height

def square_area(side):
    return side ** 2

def circle_area(radius):
    return 3.14 * ( radius ** 2 )

name = input("Your name: ")
hello()
print_welcome(name)
print()

choice = "x"
print_options()
while choice != "q":
    choice = input("Please enter your choice: ")
    if choice == "r":
        print("To find the area of a rectangle,")
        print("enter the width and height below.")
        print()
        w = positive_input("Width: ")
        h = positive_input("Height: ")

        print("Width =", w, " Height =", h, "so Area =", rectangle_area(w, h))
        print_options()

    elif choice == "s":
        print("To find the area of a square,") 
        print("enter the length of a side.")  
        print()
        side = positive_input("Side: ")

        print("Side =", side, "so Area=", square_area(side))
        print_options()

    elif choice == "c":
        print("To find the area of a circle,")
        print("enter the radius of the circle.")
        print()
        radius = positive_input("Radius: ")

        print("Radius =", radius, "so Area=", circle_area(radius))
        print_options()

    elif choice == "q":
        print(" ", end="")
    
    else:
        print("Unrecognized option.")
        print_options()