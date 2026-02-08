# A dictionary is a data type that stores data in terms of key-value pair.
# It is introduced by the use of curly braces.
# The values stored inside of a dictionary can be of any data type.
# To acces the values in a dictionary we use the keys


phonebook = {
    "Benson" : "+254 2356789" ,
    "Mary" : "+254 87894867" ,
    "victor" : "+254 564778746"
}
# showing the entire dictionary
print(phonebook)

# printing out Benson's number
print(phonebook["Benson"])

print('================')

Player = {
    "name" : "Messi",
     "Age" : "40",
     "teams" : ["PSG","Barcelona","Argentina"] ,
     "More" : {
        "children" : 6 ,
        "residence" : "US" ,
         "phonenumber" : (254676637,25467638,254686865)
     }
}
print(Player["More"]["phonenumber"][1])
# print Barcelona the second team he played for
print(Player["teams"][1])

# research on if......else statements in python