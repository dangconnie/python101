# # Exercise 1

# # Given the following dictionary, representing a mapping from names to phone numbers:

# phonebook_dict = {
#   'Alice': '703-493-1834',
#   'Bob': '857-384-1234',
#   'Elizabeth': '484-584-2923'
# }
# # Write code to do the following:

# # Print Elizabeth's phone number.
# print phonebook_dict["Elizabeth"];

# # Add a entry to the dictionary: Kareem's number is 938-489-1234.
# phonebook_dict["Kareem"] = "938-489-1234";
# print phonebook_dict;

# # Delete Alice's phone entry.
# del phonebook_dict["Alice"];
# print phonebook_dict;

# # Change Bob's phone number to '968-345-2345'.
# phonebook_dict["Bob"] = "968-345-2345";
# print phonebook_dict;

# # Print all the phone entries.
# print phonebook_dict;

# # In this exercise, are you using dynamic keys or fixed keys?




# Exercise 2: Nested Dictionaries

ramit = {
  'name': 'Ramit',
  'email': 'ramit@gmail.com',
  'interests': ['movies', 'tennis'],
  'friends': [
    {
      'name': 'Jasmine',
      'email': 'jasmine@yahoo.com',
      'interests': ['photography', 'tennis']
    },
    {
      'name': 'Jan',
      'email': 'jan@hotmail.com',
      'interests': ['movies', 'tv']
    }
  ]
}
# Write a python expression that gets the email address of Ramit.
print ramit["email"];
# Write a python expression that gets the first of Ramit's interests.
print ramit["interests"][0];
# Write a python expression that gets the email address of Jasmine.
print ramit["friends"][0]["email"];
# Write a python expression that gets the second of Jan's two interests.
print ramit["friends"][1]["interests"];
# In this exercise, are you using dynamic keys or fixed keys?





# Letter Summary

# Write a letter_histogram function that takes a word as its input, and returns a dictionary containing the tally of how many times each letter in the alphabet was used in the word. For example:

# >>> letter_histogram('banana')
# {'a': 3, 'b': 1, 'n': 2}
# In this exercise, are you using dynamic keys or fixed keys?


given_word = "banana";

def count_the_letters(given_word):
	counter = {};
	for i in given_word:
		# print i;
		# check if letter in counter matches i as you loop through the given_word
		
		if i in counter:
			# increment counter
			print "i exists"
			# increment by adding 1 to the original value, which was 1
			counter[i] = counter[i] + 1;
		else: 
			# letter is not in counter dictionary. add it.
			print "add "
			counter[i] = 1;
	print counter;

count_the_letters(given_word);






# Word Summary

# Write a word_histogram function that takes a paragraph of text as its input, and returns a dictionary containing the tally of how many times each letter in the alphabet was used in the text. For example:

# >>> word_histogram('To be or not to be')
# {'to': 2, 'be': 2, 'or': 1, 'not': 1}
# In this exercise, are you using dynamic keys or fixed keys?

# given_paragraph = "To be or not to be";

# more_split = given_paragraph.split(" ");
# print more_split;
# returns ['To', 'be', 'or', 'not', 'to', 'be'], which is a list


def count_words(given_paragraph):
	more_split = given_paragraph.lower().split();
	new_dictionary = {};
	for word in more_split:
		if word in new_dictionary:
			# increment counter
			new_dictionary[word] = new_dictionary[word] + 1;
		else:
			# word is not in counter. add it.
			new_dictionary[word] = 1;
	print new_dictionary;

print count_words("To be or not to be");







# Bonus Challenge

# Given a histogram tally (one returned from either letter_histogram or word_summary), print the top 3 words or letters.


def count_words(given_paragraph):
	more_split = given_paragraph.lower().split();
	new_dictionary = {};
	for word in more_split:
		if word in new_dictionary:
			# increment counter
			new_dictionary[word] = new_dictionary[word] + 1;
		else:
			# word is not in counter. add it.
			new_dictionary[word] = 1;
	print new_dictionary;

print count_words("To be or not to be");