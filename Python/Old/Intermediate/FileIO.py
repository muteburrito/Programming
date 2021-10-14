# File I/O stands for File input output
# File I/O is important where python needs to talk to the file read the data and then after processing it write some data in it
# 2 types of files are there:
# 1. txt file
# 2. binary file
# We have a lot of functions to read update and delete files 

# Opening a File- This is a in built function in Python
f = open('D:\Programming\Python Reference\Intermediate\sample.txt', 'r') # By default the mode is read
# Here we first put file name and location and then the operation we want to do here read
data = f.read() # We can specify how many characters of thet file we want to read by giving a number
# here f and data are two normal variables
print(data)
f.close() # We cannot perform any operaion


