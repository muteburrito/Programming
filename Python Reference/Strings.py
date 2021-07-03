x = 'This is single'
# Using dobule quotes is the most efficient way ti use strings
a = "This is Chinmay's Course"
# Here if we use single quote it will get confused

# Similarly triple quotes can help too in multiple lines and big strings

b = '''This is "Triple"
it can help in multi line string
it is helpful'''
print(x, a, b)

# We can use indexing to print a specific letter from the string like this:

index = 'Tutorial string'
#        0123456789101112   (This is how it is indexed)
print(index[0])  # This will print T

# indexing in python starts with 0,1,2,... We can use negative indexing to print characters in backwards

print(index[-1])
print(index[0:3])  # This will return values from 0 to 3 excluding 3
# if we dont specify the values and just do index[:] then it will copy whole string as default is 0 and str len
# this can be used to clone a string

clone = index[:]
