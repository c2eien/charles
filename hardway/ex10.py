#More excaping characters for strings/printing

tabby_cat = "\tI'm tabbed in." #escape a tab with \t
persian_cat = "I'm split\non a line" #escape a new line with \n
backslash_cat = "I'm \\ a \\ cat." #escape a backslash with \\
fat_cat = """ 
I'll do a list:
	\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""


print (tabby_cat)
print (persian_cat)
print(backslash_cat)
print(fat_cat)
print("test to escape quotes \' \" ")
print(''' 
what happens with 
tripple single quotes
	''')
print('percent are %r' % "\"")
print('percent ess %s' % "\"")


# Escape Sequences

# This is all of the escape sequences Python supports. You may not use many of these, but memorize their format and what they do anyway. Try them out in some strings to see if you can make them work.

# Escape	What it does.
# \\	Backslash (\)
# \'	Single-quote (')
# \"	Double-quote (")
# \a	ASCII bell (BEL)
# \b	ASCII backspace (BS)
# \f	ASCII formfeed (FF)
# \n	ASCII linefeed (LF)
# \N{name}	Character named name in the Unicode database (Unicode only)
# \r	Carriage Return (CR)
# \t	Horizontal Tab (TAB)
# \uxxxx	Character with 16-bit hex value xxxx (u'' string only)
# \Uxxxxxxxx	Character with 32-bit hex value xxxxxxxx (u'' string only)
# \v	ASCII vertical tab (VT)
# \ooo	Character with octal value ooo
# \xhh	Character with hex value hh