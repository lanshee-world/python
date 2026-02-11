def calculate_area():
    length = 10
    width = 5
    area = length * width
    print("The area of the rectangle is area: ",area)

calculate_area()
print("=================")
def arithmetics(num1,num2):
    sum = num1 + num2
    difference = num1 - num2
    product = num1 * num2
    # handle potential division by zero
    if num2 != 0:
        division = num1 / num2
    else:
        division = "cannot divide by zero"
    return sum , difference ,product , division
s, d, p, div = arithmetics(10, 5)
print(f"sum: {s}, difference: {d}, product: {p}, division: {div}")
print("===============")
def check_number_sign(number):
    if number > 0:
        print(f"The number {number} is positive.")
    elif number < 0:
        print(f"The number {number} is negative.")
    else:
        print(f"The number {number} is zero.")
    
user_input = float(input("Enter a number:"))
check_number_sign(user_input)

def calculate_sum_to_n(n):
    total_sum = 0
    for i in range(1, n + 1):
        total_sum += i
    print(f"The sum of numbers from 1 to {n} is: {total_sum}")

calculate_sum_to_n(5)

def calculate_squares(limit):
    i = 1
    while i <= limit:
        square = i * i 
        print(f"The square of {i} is: {square}")
        i += 1

user_limit = int(input("Enter number:"))
calculate_squares(user_limit)