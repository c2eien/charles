formatter = "%r %r %r %r" # defines variable formatter

print (formatter % (1,2,3,4)) #prints formatter with tuples defined
print (formatter % (formatter, formatter, formatter, formatter))
print (formatter %
	("I had this thing.",
	"That you could type up right.",
	"But it didn't sing.",
	"So I said goodnight.")
	)