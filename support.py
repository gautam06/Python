def print_func( par ):
   print "Hello : ", par
   return

def findFactorial( num ):
	temp = num
	fact = 1
	while temp > 0:
		fact = fact * temp
		temp = temp - 1
	else:
		print "Factorial of %d: %d" % (num,fact)
		

