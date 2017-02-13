counter = 0

while(counter < 5):
	print "Counter Value: ", counter
	counter += 1

#Else statement with loops

counter = 0

while counter < 5:
	print counter," is less than 5"
	counter += 1
else:
	print counter," is not less than 5"

#Single Statement Suites

#while (True): print "Infinite Loop"

#Nested While

print "Nested While Loop"

print "Find prime numbers in 1 to 100"

i = 2
while(i < 100):
	j = 2
	while(j <= (i/j)):
		if not(i%j): break
		j = j + 1
	if (j > i/j) : print i, " is prime"
	i = i + 1


print "=========================================="

#print letters of given string

print "Print Letters using For Loop\n"

for letter in 'Python':
	print 'Current Letter :', letter
	
#print list elements

print "\nPrint List Elements"

students = ['gautam', 'vimal', 'smit']

for student in students:
	print "Current student: ", student

#Iterate For Loop using index value

print "\nPrint List Elements using index"

for index in range(len(students)):
	print "Current student: ", students[index]

#Else statement in For Loop

print "\nUse of Else in For Loop"

print "Find Prime Number in  given range"

for num in range(10,20):	#iterate 10 to 20
	for i in range(2,num):	#iterate on factors
		if num % i == 0:	#find first factor
			j = num/i		#calculate second factor
			print "%d = %d * %d" % (num,i,j)
			break			#break inner loop & move next
	else:
		print num, "is a prime number"
	
#====================================================

#pass statement is a null operation

print "\npass statement example\n"

for letter in 'Python': 
   if letter == 'h':
      pass
      print 'This is pass block'
   print 'Current Letter :', letter

print "Good bye!"
