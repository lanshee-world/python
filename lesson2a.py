# A list in python is a collection of items that are ordered in a certain way. A list is introduced by the use of the square brackets [].
# The items of a list are stored inside of indexes.Note:In programming we start counting from index zero(0)
# A list is mutable i.e it's contents can be changed.
cars = ["BMW","Benz","Probox","Mclaren","Range Rover","Bentley","Rolls Royce"]
print(cars)
print(type(cars))

# Accessing items of a list
print(cars[2])
print("The car on index 4 is: ",cars[4])

# List slicing
print(cars[4:])

# printing from index zero to index three
print(cars[:4])

# printing from benz to range rover
print(cars[1:4])

# list mutability
# We use the function append to add an item at the end of the list
cars.append("Ferrari")
print(cars)
cars.append("lamborghini")
print(cars)

# we use the pop function to remove an item from the end of the list
cars.pop()
print(cars)

# we can use an index to add items to a list
cars[5] = "Neo"
print(cars)

# we can use the sort function to sort out items in alphabetical order
cars.sort()
print(cars)

