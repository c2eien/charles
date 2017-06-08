# WHILE LOOPS

#commenting out the below in order to define in function
# i = 0
# numbers = []

# while i < 6:
# 	print("At the top i is {}".format(i))
# 	numbers.append(i)

# 	i = i + 1
# 	print("Numbers now: ", numbers)
# 	print("At the bottom i is {}".format(i))

# print("The numbers: ")

# for num in numbers:
# 	print(num)

def number_lister(upper, increment):
	"""
	upper is the upper limit (non-inclusive) of the numbers listed; 
	i.e., it will stop before reaching that number
	increment is the amount it incremenets by
	"""
	i = 0
	numbers = []
	while i < upper:
		print("At the top i is {}".format(i))
		numbers.append(i)

		i = i + increment 
		print("Numbers now: ", numbers)
		print("At the bottom i is {}".format(i))

	print("The numbers: ")

	for num in numbers:
		print(num)

number_lister(6,1)
number_lister(6,2)

#doing the same thing with for loops and range, instead of while loop
def number_lister2(upper, increment):
	"""
	upper is the upper limit (non-inclusive) of the numbers listed; 
	i.e., it will stop before reaching that number
	increment is the amount it incremenets by
	"""
	numbers = []
	for i in range(0,upper,increment):
		print("At the top i is {}".format(i))
		numbers.append(i)

		i = i + increment 
		print("Numbers now: ", numbers)
		print("At the bottom i is {}".format(i))

	print("The numbers: ")

	for num in numbers:
		print(num)


number_lister2(6,1)
number_lister2(6,2)