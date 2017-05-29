from sys import argv
from os.path import exists 
# You should immediately notice that we import another handy command named exists. 
# This returns True if a file exists, based on its name in a string as an argument. 
# It returns False if not.

script, from_file, to_file = argv

open(to_file, 'w').write(open(from_file).read())
print("Alright, all done.")


