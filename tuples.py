# An array is great but it's changeable. What if you wanted something that wasn't changeable to keep programmers from breaking your code? Or you just wanted to be functional? 

# A tuple is a constant array. It's an array you can make changes to

# a_tuple = (1, 3, 8)
# print a_tuple;
# print a_tuple[2];

# does not work b/c you can't change tuples!
# a_tuple[2] = 5;

# loop through tuples the same way you do lists
# for number in a_tuple:
# 	print number;


# what you get back from mySQL is a tuple. it is unchangeable

# teams = ('falcons', 'hawks', 'atl_united', 'silverbacks');
# for team in teams:
# 	if team == "hawks":
# 		print 'Go hawks!';
# 	else:
# 		print "It's basketball season"

# team_a = "Falcons";
# print team_a == 'Falcons'

# >, <, >=, and <= are the same in Python as JS
# OR and AND work the same way, just without()
# team_b = "Braves";
# if team_a == "Falcons" and team_b == "Braves":
# 	print "Hooray"

# Alternate way
# team_b = "Braves";
# cond1 = (team_a == "Falcons"):
# cond2 = (team_b == "braves");
# if cond1 and cond2:
# 	print "Hooray"

# Python's version of indexOf is simply "in"
# print "hawks" in teams;

# for team in teams:
# 	if team == "hawks":
# 		print "Go hawks";
# 	elif team == "falcons":
# 		print "sad super bowl"

# if "hawks" in teams:
# 	print "Go hawks";
# elif "falcons" in teams:
# 	print "Go falcons";

# see this in terminal by doing python tuples.py 
# must use raw_input
# message = raw_input("Please enter your name");

height = raw_input("In inches, how tall are you? \n");
if(int(height) >= 42):
	print "You are tall enough to go on the Batman roller coaster";
else:
	print "Maybe try the kiddie coaster";



# while loop
current = 1;
# while (current < 10):
# 	print current;
	# line below does not exists in python
	# current++;
	# instead:
	# current += 1;



# traps user in loop until they type "quit". keeps going no matter what you type
answer = "play"
while answer != "quit":
	answer = raw_input("Print quit to stop the game \n");