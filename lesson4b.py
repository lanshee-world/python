# Loops- sometimes we may need to do a piece of work a number of repeated times and in such cases we use loops.
#  A loop is a control structure that allows us to create a block of repeatively until a certain condition is met.
# They are of two types: for loops and while loops
# Below is the syntax for the for loop in python;
"""
   for variable in range(n)
    # a block of code to be executed
"""
for greeting in range(5):
    print("Hello Moses")

print('==============')
for number in range(10, 20):
    print(number)
print('===============')

# Find the even numbers in the range of 50 to 71
for number in range(50, 71, 2):
    print(number)

print('=========')

# create a python program that prints the odd numbers from 100-150
for number in range(101, 150, 2):
    print(number)

print('=========')

# create a program that prints the multiples of three starting from 201 to 150
for number in range(201, 149, -1):
    if number % 3 ==0:
     print(number)
print('=========')
# create a python program that prints the leap years in between the year 2000 to 2024
for number in range(2004, 2024):
    if number % 4 == 0:
        print(number)