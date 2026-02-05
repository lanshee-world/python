# A tuple is an immutable type of list(it cannot change)
# to introduce a tuple we use parenthesis
counties = ("Nairobi","Mombasa","Kisumu","Nakuru","Kajiado","Eldoret")
print(counties)
print(counties[3:])

# Accessing items of a tuple by use of the indexes
print(counties[2])

# Note:Below will generate an error
# Attribute error
counties.append("Machakos")