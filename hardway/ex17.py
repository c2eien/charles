from sys import argv
from os.path import exists 
# You should immediately notice that we import another handy command named exists. 
# This returns True if a file exists, based on its name in a string as an argument. 
# It returns False if not.

script, from_file, to_file = argv

print("Copying from {} to {}".format(from_file, to_file))

# we could do these two on one line, how?
# in_file = open(from_file)
# indata = in_file.read()

indata = open(from_file).read()

print("The input file is {} bytes long".format(len(indata)))

print("Does the output file exist? {}".format(exists(to_file)))
print("Ready, hit RETURN to continue, CTRL-C to abort.")

input()

out_file = open(to_file, 'w')
out_file.write(indata)

print("Alright, all done.")

out_file.close()

