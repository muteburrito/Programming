# While loop has following syntax:
# while 'condition': here the condition can be statement or a bollean value also
# Block of code tp be executed
## i = 1
# while i <= 5:  # Here we define the while loop that do the below steps while the condition is i < 5
# print(i)
# i = i + 1  # If we dont give this line it will end up in a infinite loop
# print('Done')
##
# So in general this made the printing of a number which was repetative easier

# Now lets create a star pattern:
i = 1
while i <= 5:
    print('*' * i)  # Now as we now if we put an astrix in front of a string and give it a number it will print that string those many times
    i = i + 1
print('Done')
