# this one is like your scripts with argv
def print_two(*args):
	arg1, arg2 = args
	print("arg1: {}, arg2: {}".format(arg1, arg2))
#this is not a good way. 
# The problem with print_two is that it's not the easiest way to make a function. 
# In Python we can skip the whole unpacking arguments 
# and just use the names we want right inside (). 


# ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
	print("arg1: {}, arg2: {}".format(arg1, arg2))

# this just takes one argument
def print_one(arg1):
	print("arg1: {}".format(arg1))

# no arguments
def print_none():
	print("Nothing")

print_two("thingy", "shwat")
print_two_again("chill","OUT")
print_one("schlooop")
print_none()