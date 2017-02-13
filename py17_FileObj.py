#file object = open(file_name [, access_mode][, buffering])

#file_name: name of the file that you want to access

#access_mode: i.e., read, write, append, etc. default mode is read (r).

#buffering: 0 = no buffering, 1 = line buffering. 
#if buffering > 1, then buffering action is performed with the indicated buffer size. 
#if negative, the buffer size is the system default(default behavior).


# r		Opens a file for reading only. The file pointer is placed at the beginning of the file. This is the default mode.
# rb	Opens a file for reading only in binary format. The file pointer is placed at the beginning of the file. This is the default mode.
# r+	Opens a file for both reading and writing. The file pointer placed at the beginning of the file.
# rb+	Opens a file for both reading and writing in binary format. The file pointer placed at the beginning of the file.
# w		Opens a file for writing only. Overwrites the file if the file exists. If the file does not exist, creates a new file for writing.
# wb	Opens a file for writing only in binary format. Overwrites the file if the file exists. If the file does not exist, creates a new file for writing.
# w+	Opens a file for both writing and reading. Overwrites the existing file if the file exists. If the file does not exist, creates a new file for reading and writing.
# wb+	Opens a file for both writing and reading in binary format. Overwrites the existing file if the file exists. If the file does not exist, creates a new file for reading and writing.
# a		Opens a file for appending. The file pointer is at the end of the file if the file exists. That is, the file is in the append mode. If the file does not exist, it creates a new file for writing.
# ab	Opens a file for appending in binary format. The file pointer is at the end of the file if the file exists. That is, the file is in the append mode. If the file does not exist, it creates a new file for writing.
# a+	Opens a file for both appending and reading. The file pointer is at the end of the file if the file exists. The file opens in the append mode. If the file does not exist, it creates a new file for reading and writing.
# ab+	Opens a file for both appending and reading in binary format. The file pointer is at the end of the file if the file exists. The file opens in the append mode. If the file does not exist, it creates a new file for reading and writing.

# Open a file
fileg = open("fileg.txt", "wb")
print "Name of the file: ", fileg.name
print "Closed or not : ", fileg.closed
print "Opening mode : ", fileg.mode
print "Softspace flag : ", fileg.softspace

fileg.close();
print "Closed or not : ", fileg.closed


# Open a file
fo = open("fileg.txt", "wb")
fo.write( "Python is a great language.\nYeah its great!!\n");

# Close opend file
fo.close()


# Open a file & read specified number of bytes if empty read as possible as may be whole file
fo = open("fileg.txt", "r+")
str = fo.read(10);
print "Read String is : ", str
# Close opend file
fo.close()


# tell() & seek() example

# Open a file
fo = open("fileg.txt", "r+")
str = fo.read(10);
print "Read String is : ", str

# Check current position
position = fo.tell();
print "Current file position : ", position

# Reposition pointer at the beginning once again
position = fo.seek(0, 0);
str = fo.read(10);
print "Again read String is : ", str
# Close opend file
fo.close()

#Rename File

# import os
# os.rename( "test1.txt", "test2.txt" )

#Remove File

# import os
# os.remove("text2.txt")

#Create new directory
# os.mkdir("newdir")


#chdir() Method
#change the current directory

# import os
# os.chdir("/home/newdir")


#getcwd() displays the current working directory.
# os.getcwd()

#rmdir() method deletes the directory.
#Before removing a directory, all the contents in it should be removed.

# import os
# os.rmdir( "/tmp/test"  )


#writing in file

# Open a file in write mode
fo = open("demo.txt", "rw+")
print "Name of the file: ", fo.name

# Assuming file has following 5 lines
# This is 1st line
# This is 2nd line
# This is 3rd line
# This is 4th line
# This is 5th line

str = "This is 6th line"
# Write a line at the end of the file.
fo.seek(0, 2)
line = fo.write( str )

# Now read complete file from beginning.
fo.seek(0,0)
for index in range(6):
   line = fo.next()
   print "Line No %d - %s" % (index, line)

# Close opend file
fo.close()

#Other Functions for file operation


#file.close()
#Close the file. A closed file cannot be read or written any more.
	
#file.flush()
#Flush the internal buffer, like stdio's fflush. This may be a no-op on some file-like objects.
	
#file.fileno()
#Returns the integer file descriptor that is used by the underlying implementation to request I/O operations from the operating system.

#file.isatty()
#Returns True if the file is connected to a tty(-like) device, else False.

#file.next()
#Returns the next line from the file each time it is being called.

#file.read([size])
#Reads at most size bytes from the file (less if the read hits EOF before obtaining size bytes).

#file.readline([size])
#Reads one entire line from the file. A trailing newline character is kept in the string.

#file.readlines([sizehint])
#Reads until EOF using readline() and return a list containing the lines. If the optional sizehint argument is present, instead of reading up to EOF, whole lines totalling approximately sizehint bytes (possibly after rounding up to an internal buffer size) are read.

#file.seek(offset[, whence])
#Sets the file's current position
	
#file.tell()
#Returns the file's current position

#file.truncate([size])
#Truncates the file's size. If the optional size argument is present, the file is truncated to (at most) that size.

#file.write(str)
#Writes a string to the file. There is no return value.

#file.writelines(sequence)
#Writes a sequence of strings to the file. The sequence can be any iterable object producing strings, typically a list of strings.
