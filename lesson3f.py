# Create a python program that is able is able to determine whether a number entered is an odd number or an even number.
number = int(input("Enter your number"))
if number % 2 == 0:
    print("even number")
else:
    print("odd number")

# Create a python program that is able to determine whether a person can donate blood based on the age and weight of a person.. If the weight is greater than 50kg and age is above 18, then the person can donate ,else not possible.
age = int(input("Enter age here"))
weight = float(input("Enter weight here"))
if age > 18 and weight > 50:
    print("can donate")
else:
    print("cannot donate")