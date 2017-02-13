#functions for Data Type Conversion

x = "66"
y = 4

#convert string to int

#======================================================

add = int(x,10) + y

print "addition: ", add

#======================================================

#convert int to String

z = 6

#Below line gives error not concatnation into string
#print "There are "+ z +" colleges for MCA"

print "There are "+str(z)+" colleges for MCA"

#Example string vs repr

#Example 1

s = 'Hello, Geeks.'
print str(s)
print str(2.0/11.0)

s = 'Hello, Geeks.'
print repr(s)
print repr(2.0/11.0)

#Example 2 USing Data Time

import datetime
today = datetime.datetime.now()
 
# Prints readable format for date-time object
print "Readable Format using str() = "+str(today)
 
# prints the official format of date-time object
print "Official Format using repr() = "+repr(today)   

#======================================================

#Eval Example

#eg. input = x * 2

user_func = raw_input("type a function: y = ")

for x in range(1,10):
	print "x = ", x , ", y = ", eval(user_func)

#======================================================

#other functions available listed below

#tuple(s) 	#Converts s to a tuple.

#list(s) 	#Converts s to a list.

#set(s) 	#Converts s to a set.

#dict(d)	#Creates a dictionary. d must be a sequence of (key,value) tuples.

#frozenset(s) #Converts s to a frozen set.

#chr(x) 	#Converts an integer to a character.

#unichr(x)	#Converts an integer to a Unicode character.

#ord(x)		#Converts a single character to its integer value.

#hex(x)		#Converts an integer to a hexadecimal string.

#oct(x)		#Converts an integer to an octal string.



