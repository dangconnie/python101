# 1) Sum the Numbers

# Given an list of numbers, print their sum. When I say given something, just make something up and store it in a variable.

numbers = [1,2,3,4,5,6,7];
sumNumbers = sum(numbers);
print sumNumbers;



# 2) Largest Number

# Given an list of numbers, print the largest of the numbers.

numbers = [5,10,3,4,6];

numbers.sort();
print numbers;
print numbers[-1];



# 3) Smallest Number

# Given an list of numbers, print the smallest of the numbers.
numbers = [5,10,3,4,6];

numbers.sort();
print numbers;
print numbers[0];



# 4) Even Numbers

# Given an list of numbers, print each number in the list that is even.

numbers = [5,10,3,4,6,8,2];

for i in numbers:
	if (i%2 == 0):
		print i;



# 5) Positive Numbers

# Given an list of numbers, print each number in the list that is greater than zero.
numbers = [5,10,-1, 3,4,-16,8,2,-9];

for i in numbers:
	if(i>0):
		print i;





# 6) Positive Numbers II

# Given an list of numbers, create a new list which contains every number in the given list which is positive.
numbers = [5,10,-1, 3,4,-16,8,2,-9];

new_positive_numbers=[];

for i in numbers:
	if(i>0):
		new_positive_numbers.append(i);
print new_positive_numbers;





# 7) Multiply an list

# Given an list of numbers, and a single factor (also a number), create a new list consisting of each of the numbers in the first list multiplied by the factor. Print this list using console.log(list);
numbers = [5,10,-1, 3,4,-16,8,2,-9];

new_multiplied_numbers=[];

factor = 3;

for i in numbers:
	new_multiplied_numbers.append(i*3);
print new_multiplied_numbers;



# 8) Multiply Vectors

# Given two lists of numbers of the same length, create a new list by multiplying the pairs of numbers in corresponding positions in the two lists. Example:

# [2, 4, 5] x [2, 3, 6] = [4, 12, 30]

list1 = [1, 2, 3];
list2 = [4, 5, 6];
new_list = [];

for i in range(0, len(list1)):
	new_list.append(list1[i]*list2[i])
print new_list;




# 9) Matrix Addition

# Given two two-dimensional lists of numbers of the size 2x2 two dimensional list is represented as an list of lists:

# [ [2, -2],
#   [5, 3] ]
# Calculate the result of adding the two matrices. The number in each position in the resulting matrix should be the sum of the numbers in the corresponding addend matrices. Example: to add

# 1 3
# 2 4
# and

# 5 2
# 1 0
# results in

# 6 5
# 3 4



list = [[1,2],[3,4],[5,6],[7,8]];
list1=[];
list2=[];
new_list=[];

for i in range(0, len(list[0])):
	list1.append(list[0][i] + list[2][i]); 
	list2.append(list[1][i] + list[3][i]);
	print list1;
	print list2;
	new_list = [list1, list2];

print new_list;




#10)Matrix Addition II

# Use your solution in Matrix Addition, and extend it to work for a pair of matrices of any size, as long as they have the same size.

list = [[1,2,3,10,11,89],[3,4,5,10,3,6],[5,6,7,10,3,6],[7,8,9,10,3,6]];
list1=[];
list2=[];
new_list=[];

for i in range(0, len(list[0])):
	list1.append(list[0][i] + list[2][i]); 
	list2.append(list[1][i] + list[3][i]);
	new_list = [list1, list2];

print new_list;




# 11) De-dup

# Given an list of numbers or strings, create a new list containing the same elements as the first list, except with any duplicate values removed. Print the list.

numbers = [5,5,10,1,3,4,4,16,8,8,2,9,9];
new_list = [];
	for i in numbers:
		for j in new_list:
			if (numbers[i] == new_list[j]):
				numbers.remove(i);
				new_list.append(j);
print new_list;




# 12) Bonus: Matrix Multiplication

# Given two two-dimensional lists of numbers of the size 2x2 - calculate the result of multiplying the two matrices. Print the resulting matrix. How do you multiple two matricies? https://www.khanacademy.org/math/precalculus/precalc-matrices/multiplying-matrices-by-matrices/v/matrix-multiplication-intro