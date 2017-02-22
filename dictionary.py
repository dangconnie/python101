# dictionary is the fancy Python term for a JS object


# must put keys (properties in JS) in quotes
# var x ={
# 	"name": "Connie",
# 	"gender": "female"
# }



# In python, they're called key-value pairs. In js, it is (property, value)
zombie = {
	"speed": 10,
	"power": 6,
	"hunger": 12,
	"name": "zombie",
	"age": "varies",
	"defense": 0
}

# in python, you can't do zombie.speed. if you want to access those keys, use brackets
print zombie["speed"];



# You can add a new key just like you do in JS. Vars are dynamic in Python!
# weapon and starting position addded to zombie
zombie["weapon"] = "fist";
zombie["startX"] = 200;
zombie["startY"] = 100;
print zombie;


# Change the value of an existing key just like JS
if zombie["speed"] < 5:
	zombie["position"] = zombie["startX"] + 2;
elif zombie["speed"] < 10:
	zombie["position"] = zombie["startX"] + 4;
else:
	zombie["position"] = zombie["startX"] + 6;

# you can delete a key with delete
zombie["pointless"] = "duh";
del zombie["pointless"];
print zombie;


# Store all the techs we know in a dictionary and set the value from 1-10
skill1 = "Redux";

techs = {
	"spells":["fire", "ice"],
	"JS": 7,
	"node": 6,
	"Python": 10,
	"React":2,
	skill1: 4
}
print techs;


# for loops through dictionaries, start with key (placeholder), value
# in this case, we don't have an array
for key, value in techs.items():
	print key;

# "students" is assumed to be an array in js for this to work
	# students.map(student, index)=>{
		
	# }


# check if key exists:
if zombie.has_key('mother_name'):
	print zombie["mother_name"];

# we don't have indices. we have strings but we can still access them like indices. Looping through key values in the dictionary
for key in zombie:
	print zombie[key]



# just like in JS, you can put dicitonaries inside of lists (objects in arrays)
zombies = [];
zombies.append({
	"speed": 10,
	"power": 6,
	"hunger": 5,
	"name": "Bill"
})
zombies.append({
	"speed": 5,
	"power": 16,
	"hunger": 9,
	"name": "Sven"
})

print zombies;
print zombies[0];
# prints off name of zombie at index 0
print zombies[0]["name"];


for zombie in zombies:
	print zombie["name"];


# just like JS objects, you can assign a list to a dictionary key
zombies[0]["victims"] = ['Sean', "Rishi", "Anna"];
print zombies[0];

# prints off first element in list: "Sean"
print zombies[0]["victims"][0];


zombies[0]["victims"] = [{}, "Rishi", "Anna"];
zombies[0]["victims"][0]["name"] = "Sean";
print zombies[0];

# Just like in JS, you assign a dictionary to a dictionary
# zombie[0]["at_night"] = {
# 	"power": 23,
# 	"hunger": 20,
# 	"weapon": "baseball bat"
# }