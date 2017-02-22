# have user guess random numbers between 1-10. User is stuck in the loop of guessing until they get the nuber right or type "give up"



#can't use randint without importing 
from random import randint

# generate random number
number_to_guess = randint(1,10);

# ask for user_input guess
user_input = raw_input("Enter your guess between 1-10. \n");

# def number_to_guess():
# 	print randint(1,10)
# number_to_guess();

# make user stuck in loop because it's fun
answer = number_to_guess;
while user_input != answer:
	print int(raw_input("Wrong. Keep guessing.Type" + answer + " to quit."))
