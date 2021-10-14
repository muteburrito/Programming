# Functions are set of code which perform a specific task
# In short we use function to group a code 
# There are 2 types of functions:
# 1- Built in Functions and 2- User Defined Functions
# built in include print, input, etc 

# Lets say we want addition of numbers

def addsum(num): # This is the way we define a function in python

    add = (num[0] + num[1] + num[2] + num[3]) # this is general statement 
    return(add) # This will return the sum

def Hello():
    print('Hello World') # This is Function defination

list1 = [55, 78, 34, 44]
addition = addsum(list1) # This is called function call
print(addition)
Hello() # Function call
# So here we can use this function any where n the program to add.
# In this way functions can be used to make coding easier and faster 
# Function can be reused any number of times in the full program


# We can have default value of a function too, which will be used in case we dont provide a input
# This is called default parameter value
def greet(name = 'Guest'): # here if we dont give any name it will use this as default value
    print(f'Hello {name}')

greet() # If we had not given default value it would have given an error 
