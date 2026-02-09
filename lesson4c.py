# A for loop can also be used to iterate through a list,tuple,string or even a dicionary...

name = "Keya"
for letter in name:
   if letter == "e":
      print("This is letter e")
   else:
      print(letter)
print('=========')

# Below is a list of counties
counties = ("Nairobi","Mombasa","Kisumu","Nakuru","Eldoret","Kajiado","Machakos","Meru","Embu")
for county in counties:
   print(county)
print('=========')
if "Nakuru" in counties:
       print("county found")
else:
       print("county not found")
print('=========')

# the for loop can also be used to iterate through a dictionary
player = {
    "name" : "Mbappe",
    "age" : 25,
    "teams" : ["PSG","Monaco","France"],
    "nationality" : "French"
}
for values in player:
    print(player[values])
print('=========')

for team in player["teams"]:
    print(team)