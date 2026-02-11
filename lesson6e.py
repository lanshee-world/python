# On the try and except block,you run some codes/statements and if it is successful the try block will be executed other the except block will be executed when there is an anticipated error.

try:
    number = 100
    answer = number / 0
    print(answer)
except Exception as e:
    print("There is an error", e)