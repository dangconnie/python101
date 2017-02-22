# 1) 1 to 10

# Using a for loop and the range function, print out the numbers between 1 and 10 inclusive, one on a line. 

for i in range(1,10):
	print i;




# 2) n to m

# Same as the previous problem, except you will prompt the user for the number to start on and the number to end on. 

def user_loop():

	user_start_input = int(raw_input("What number should we start with?"));

	user_end_input = int(raw_input("What number should we end with?"));

	for i in range(user_start_input, (1+ user_end_input)):
		print i;

user_loop();	






# 3) Odd Numbers

# Print each odd number between 1 and 10 inclusive. Example output:

 
for i in range (1,11,2):
	print i;



# 4) Print a Square

# Print a 5x5 square of * characters. 

for i in range(0,4):
	print ("*****");




# 5) Print a Square II

# Print a NxN square of * characters. Prompt the user for N. 


# first loop: how many times we want it to print
# second loop: how many times to build it
def print_the_square():
	user_n = raw_input("How big should this square be?");

	for i in range(0, int(user_n)):
		empty_string = '';
		for i in range(0, int(user_n)):
			empty_string += "*";
		print empty_string;

print_the_square();




# 6) Print a Box

# Given a height and width, input by the user, print a box consisting of * characters as its border. 


def print_a_box():
	height = raw_input("How tall should the box be? \n");
	width = raw_input("How fat should the box be?\n");

	take width and make that specify the number of stars in the top and bottom rows
	for i in range(0,int(height)):
		print full string of stars only for the first and last rows
		if(i==0 or i == int(height)-1):
			empty_string = "";
			for j in range(0, int(width)):
				empty_string += "*";
			print empty_string;
		else:
			empty_string = "*";
			for j in range(0, int(width)-2):
				empty_string += " ";
			print empty_string + "*";
print_a_box();



#7) Print a triangle consisting of * characters

for i in range(0,11,2):
	empty_string = "";
	for j in range(0, i+1):
		empty_string += "*";
	print empty_string;	








# 8) Print a Triangle II

# Given a number as the height, print a triangle as in "Print a Triangle" but with the given height.









# 9) Multiplication Table

# Print the multiplication table for numbers from 1 up to 10. Example output:

# $ python multiplication_table.py
# 1 X 1 = 1
# 1 X 2 = 2
# 1 X 3 = 3
# 1 X 4 = 4
# ...
# 5 X 5 = 25
# 5 X 6 = 30
# 5 X 7 = 35
# ...
# 10 X 8 = 80
# 10 X 9 = 90
# 10 X 10 = 100
# Bonus: Print a Banner









#10) Given a string, input by the user, print that string with a box around it. The box should stretch to the length of the string. Example session:

# $ python banner.py
# Text? Welcome to DigitalCrafts
# ****************************
# * Welcome to DigitalCrafts *
# ****************************
# Bonus: Triangle Numbers








# 11) Print the first 100 triangle numbers. What is a triangle number? Read this: https://www.mathsisfun.com/algebra/triangular-numbers.html.








# 12) Bonus: Factor a Number

# Given a number, print its factors. What are factors? https://www.khanacademy.org/math/pre-algebra/factors-multiples/divisibility-and-factors/v/finding-factors-of-a-number