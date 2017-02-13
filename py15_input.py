#The raw_input([prompt]) function reads one line from standard input 
# and returns it as a string (removing the trailing newline).

str = raw_input("Enter your input: ");
print "Received input is : ", str

#The input([prompt]) function is equivalent to raw_input, 
#except that it assumes the input is a valid Python expression and returns the evaluated result to you.

str = input("Enter your input: ");
print "Received input is : ", str




