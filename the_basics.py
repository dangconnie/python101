# print "Connie Dang"

# no var, no initialization in python. all happens at once. python is synchronous. 

# you don't have to worry about hoisting in python as in you don't even have var in python. semicolons optional (like js). just make sure stuff exists.

# python isn't running inside the browser. print statements will print to terminal or print below

# name = "Connie Dang";
# name = "Connie " + "Dang";

# forty_two = 40 + 2;
# print forty_two;

# forty_two = 84 / 2;
# print forty_two;

# forty_two = 83 %2;
# print forty_two;


# Array Lists (in Python)
# has to be a whole number
animals = [
	'wolf', 
	'giraffe', 
	'hippo'
];
# print animals;
# print animals[0];
# -1 indicates last one in array
# print animals[-1];


# How do we push new elements on a list?? Use append!
animals.append("Alligator");
print animals;


# To delete an index, use remove method
animals.remove("wolf");
print animals;

# We can insert into any indice with "insert" method. This is specific to lists.

# inserted zebra at the beginning of the list
animals.insert(0, 'zebra');
print animals;


# below overwrites index
animals[0] = "horse"
print animals;

# deletes 0 index
del animals[0]
print animals;

# Pop works the same way as js.....removes the last elements
animals.pop()
print animals;

# split works the same way as well
dc_class = "Michael, Paul, Mason, Casey, Connie, Sarah, Andy";
# split where there is a comma
dc_class_as_array = dc_class.split(", ");
print dc_class_as_array;

# Sorted method will sort but will not change the actual array
# sorted but not mutated
sorted_class = sorted(dc_class_as_array)
print sorted(dc_class_as_array)
# original array stays the same:
print dc_class_as_array

# sort method WILL mutate it
dc_class_as_array.sort();
print dc_class_as_array;


# reverse method reverses the array on the index, but not on value (unlike js)
dc_class_as_array.reverse();
print dc_class_as_array;


# len attribute: works like .length in js
print len(dc_class_as_array);

# go directly to elements
print dc_class_as_array[0];


# slice in js is [x:x] in python
# goes to xth (2) element and stops at x (4). inclusive of first number, exclusive of second number
# this creates a copy of the array. it does not mutate the array.
# print dc_class_as_array[2:4]


# For loop is [for] [what_you_call_each_one] [in] [var] 
# no brackets!! use colon instead
# for student in dc_class_as_array:
	# indentation matters in python!!
	# print student;

# two other ways to write a for loop:
# will run for 1-10. will start on 1 and will stop exclusive of 10
# for i in range(1,10)
	# print i;

# this is the long way of doing lines 101-103
# for i in range(1,len(dc_class_as_array)):
	# print dc_class_as_array[i];

# a function in python is not a function. it is a "definition", ergo, def:
# def sayHello():
	# just like for loops, : is the {} in python for functions
	# print "Hello, World";
# sayHello();

def say_hello_with_name(name, state = []):
	print "Hello, " + name
name = "Connie"
# can only take one argument
say_hello_with_name(name);