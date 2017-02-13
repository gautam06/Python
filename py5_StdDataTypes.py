#Python Standard DataTypes

print "Numbers String List Tuple Dictionary"

print "Numbers -> int (-1,786,-0x260,0x69), float(15.20,-25.1,-32.3e100), complex(3.14j, .876j, 4.53e-7j)"

print ""

#Number Examples

print ("\n-------------------------------------")

print ("Number Exaples");

print ("-------------------------------------")

var1 = 1
var2 = 10

print "var1: ",var1

print "var2: ",var2

#One can delete reference to a object by del statement

del var1;	#delete reference

#or del var1, var2

#Below line gives error var1 not defined
#print "var1: ",var1

#String Examples ------------------------

s = "Indian Hero Saktiman"

print ("\n-------------------------------------")

print ("String Examples")

print ("-------------------------------------")

print (s) 		#print complete string
print (s[0]) 	#print first character
print (s[7:11]) #print characters from 7 to 10
print (s[7:])	#print string starting from 7
print (s * 2)	#print string two times
print (s + " The Real Hero") #print concatenated string

#List Examples ----------------------------

print ("\n-------------------------------------")

print ("List Examples")

print("-------------------------------------")
list = [ 'abcd ', 786 , 23.36,'gautam',70.2]

tinylist =[123,'gautam']

print (list)		#prints complete list
print (list[0])		#prints first element of list
print (list[0:3])	#prints elements 1st to 3rd
print (list[3:])	#prints elements starting from 4
print (tinylist * 2) #print list two times
print (list + tinylist) #prints concatenated lists

print ("Changing value in touple")

list[2] = 66.06 #possible to change value

print (list)

#Tuples Examples ----------------------------

print ("\n-------------------------------------")

print ("Tuples Examples")

print ("-------------------------------------")

print ("Tuples are enclosed within parenthesis\n")

tuple = ( 'abcd', 786, 2.23, 'gautam', 70.2)

tinytuple = (123,'gautam')

print (tuple)		#prints complete tuple
print (tuple[0])	#prints first element of tuple
print (tuple[0:3])	#prints elements 1st to 3rd
print (tuple[3:])	#prints elements starting from 4
print (tinytuple * 2) #print tuple two times
print (tuple + tinytuple) #prints concatenated tuples

#Below code gives error as it does not support modification

#tuple[2] = 1000

#Dictionary Examples ----------------------------

print ("Dictionary is kind of Hash-Table Type")

print ("Dictionary works like associative array") 

print ("\n-------------------------------------")

print ("Dictionary Examples")

print ("-------------------------------------")

dict = {}
dict['one'] = "one"
dict[2] = "two"

tinydict = {'name':'gautam','college':'rollwala computer center','code':3245}

print (dict['one'])		#prints value for 'one' key
print (dict[2])			#prints value for 2 key
print (tinydict)		#prints complete dictionary
print (tinydict.keys())	#prints all the keys
print (tinydict.values())	#prints all the values
