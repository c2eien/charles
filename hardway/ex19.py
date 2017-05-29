def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print("You have {} cheeses!".format(cheese_count))
	print("You have {} boxes of crackers.".format(boxes_of_crackers))
	print("geet a blanket.\n")

print("We can just give the function numbers directly:")

cheese_and_crackers(input("how many cheese: "), input("how many crackers: "))

print("Or we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print("We can do math inside too")
cheese_and_crackers(10+20, 5*10)

print("We can do variables and math")
cheese_and_crackers(amount_of_cheese +1, amount_of_crackers+90)