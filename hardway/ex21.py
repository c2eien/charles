def add(a, b):
	print("Adding {} + {}".format(a,b))
	return a+b

def subtract(a,b):
	print("SUBTRACTING {} - {}".format(a,b))
	return a-b

def multiply(a, b):
	print("MuLTIPLYING {} * {}".format(a,b))
	return a*b

def divide(a,b):
	print("DIVIDING {} / {}".format(a,b))
	return a/b

print("Let's do some math with just functions!")

age = add(float(input()), float(input()))
height = subtract(78, 4)
weight = multiply(90,2)
iq = divide(100,2)

print("Age: {}, Height: {}, Weight: {}, IQ: {}".format(age, height, weight, iq))

# A puzzle for extra credit
print("Here is a puzzle")
what = add(age, subtract(height, multiply(weight,divide(iq,2))))

print("That becomes: ", what, "can you do it by hand?")




