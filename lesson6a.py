# MODULES
# a python module is a file that contains python definitions and/or functions.
def add():
    num1 = 20
    num2 = 30
    sum = num1 + num2
    print(sum)

def subtract():
    num1 = 20
    num2 = 30
    difference = num1 - num2
    print(difference)

def rectangle_area():
    length = int(input("Enter the length of the rectangle : "))
    width = int(input("Enter the width of the rectange : "))
    area = length * width
    print("The area of the rectangle is: ", area)

# This functions defined above on this particular file can be called into another file.
