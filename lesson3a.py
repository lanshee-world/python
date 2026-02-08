# Boolean-this is a datatype that evaluates either to true or false.
isRaining = False
print(isRaining)
print(type(isRaining))

paidloan = True
print(paidloan)

# comparison operators:They are used to compare two or more statements and they usually return a boolean answer.
number1 = 2
number2 = 5
print("Is number1 greater than number2?", number1 > number2)
print("Is number1 less than number2?", number1 < number2)
print("Is number1 greater than or equal to number2?", number1 >= number2)
print("Is number1 less than or equal to number2?", number1 <= number2)
print("Is number1 equal to number2?", number1 == number2)
print("Is number1 not equal to number2?", number1 != number2)

# logical operators
# logical AND
# It returns true if and only the condition/statements evaluates to true
print(3 > 1) and (7 > 6)

# logical OR
# It evaluates to true if one of the statements or conditions evaluates to true
print(3 > 1) or (7 < 6)

# logical NOT
# It is used to negate a statement/condition
print(not(90 > 70))