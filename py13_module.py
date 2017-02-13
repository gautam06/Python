#!/usr/bin/python

# Import module support
import support

# Now you can call defined function that module as follows
support.print_func("Gautam")

from support import findFactorial 

print support.findFactorial(5)

#Locating Modules
#When you import a module, the Python interpreter searches for the module in the following sequences

#First -> The current directory.

#Second -> The shell variable PYTHONPATH

#Third -> default path /usr/local/lib/python/.

print "================================================================="

print "Use of dir()"

# Import built-in module math
import math

content = dir(math)

print content

#reload

reload(support) #use for reloading module
