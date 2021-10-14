# For loops are basically used to iterate or run a loop with regards to a sequence like list tuple etc
# Like content of list can be traversed in the loop in a easier manner

fruits = ['Banana', 'Mango', 'Apple', 'Watermelon']

for i in fruits:
    print(i)
# This made printing easy

# We can define a range with the help of range function

for i in range(1, 9, 2): # Here it will start from 1 and will end at 8 as it prints n-1, the 2 indicates 
# step size so after 1 it will print 3
    print(i)
# We can also start from 2,3,... and so on 

# Also we can have optional else after for loop and while loop is completed. This is useful only when 
# we want to get a status for successful loop completion if we have a break in between loop the else statement is not executed