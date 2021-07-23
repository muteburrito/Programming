from os import fdopen


f = open('D:\Programming\Python Reference\Intermediate\sample.txt', 'r')
line1 = f.readline()
# This method will print 1st line
print(line1)
line2 = f.readline()
print(line2)
lines = f.readlines()
print(lines)
f.close()

# We can open file in different types:
# Read - r, Write - w, Append - a, Updating - +
# If we want to work on binary mode we will write rb and for text files rt is already present

# To write a file we need to go in append or write mode :
f = open('D:\Programming\Python Reference\Intermediate\sample.txt', 'w') # If a file is not present the code will create it also
f.write('Please write 2 this to the file')
f.close()

# The write function overwrites the file so to prevent that we use append;
f = open('D:\Programming\Python Reference\Intermediate\ another.txt', 'w')
f.write('Hello World')
f.close()
f = open('D:\Programming\Python Reference\Intermediate\ another.txt', 'a')
f.write('Append')
f.close()
