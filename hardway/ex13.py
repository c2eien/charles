from sys import argv

# argv is a MODULE that allows you to pass variables through the command line
# so you run this file from the command line like this: "python ex13.py 1st 2nd 3rd"
# where 1st 2nd 3rd are the variables after the script name

print(argv)

script, first, second, third = argv
# this unpacks/maps the given arguments to respective variables


print ("The script is called:", script)
print("Your first variavle is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)

