# functions with parameters
# Parameters- are values that get passed as arguments when given to a function inside of the parentheses.
def greeting(name):
    print(f"{name} How are you? Hope everything is fine.")
greeting("Fidel")
print("=================")

def message(names):
    print(f"Hello {names}.We shall be having a general meeting on date...Please avail yourself.")

message("Kim")
message("Joshua")
print("================")
# create a function that accepts parameters to add two numbers
def add(x,y):
    sum = x + y
    
    print(sum)
    
add(3, 4)
