from sys import argv

script, filename = argv

txt = open(filename)

print("Here's your file {}:".format(filename))
print(txt.read()) # "reads" the txt file that is variable "txt" and prints it out. 
# so .read is a method that can be used on txt files

print("Type the filename again:")
file_again = input("> ")
# user could also respond with a new file name here.

txt_again = open(file_again)
print(txt_again.read())

txt.close()
txt_again.close()