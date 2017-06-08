# IF ELIF ELSE

print("You enter a dark room with two doors. Do you go through door #1 or door #2?")

door = input("> ")

if door == "1":
	print("There's a giant bear eating a cheesecake. What do you do?")
	print("1. Take the cake.")
	print("2. Scream at the bear.")

	bear = input("> ")

	if bear == "1":
		print("The bear eats your face off.")
	elif bear =="2":
		print("The bear eats your legs off.")
	else: 
		print("Oh, {}. That's good. Bear runs away.".format(bear))

elif door == "2":
	print("You stare into the endless abyss.")
	print("1. blueberries.")
	print("2. poop")
	print("3. three")

	insanity = input("> ")

	if insanity == "1" or insanity =="2":
		print("Your mind is jello.")
	else:
		print("You did it.")

else:
	print("Your clumsy.")

