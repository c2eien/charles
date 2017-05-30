print("Let's practice everything.")
print('You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs/')

poem = """
\tThe lovely world
with logic something blah
discern \n blah ttee
\n\t\twhere there is non
"""

print("---------------")
print(poem)
print("---------------")

five = 10-2 + 3-6
print("This should be five: {}".format(five))

def secret_formula(started):
	jelly_beans = started*500
	jars = jelly_beans/1000
	crates = jars/100
	return jelly_beans, jars, crates

start_point = 10000
beans, jars, crates = secret_formula(start_point)

print("With a starting point of: {}".format(start_point))
print("We'd have {} beans, {} jars, and {} crates.".format(beans, jars, crates))

# start_point = start_point/10
start_point /= 10

print("We can also do that this way:")
print("We'd have {} beans, {} jars, and {} crates.".format(*secret_formula(start_point)))
# NOTE: we had to use a * in .format argument to get it to recognize the returned tuple 
#  as multiple arguments rather than a single argument
