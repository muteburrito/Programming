# We have many functions for strings

a = 'Hello World'
print(len(a))  # This method will return the length of that string
# To view more functions we can write the variable name followed by a dot
print(a.upper())  # Every function must be followed with a paranthesis

# The above function will print the string in a upper case format
# This method does not change the original variable

print(a)
print(a.lower())
# We can use the find method to find a character in the string, this method will return the the index of that character
print(a.find('W'))  # Anything we pass in the find method must be in quotes

# We also have a function to replace:
print(a.replace('World', 'Universe'))
# Most of the methods are case sensitive.

# This expression will give bollean value and check if that string is present in the variable
print('World' in a)
# Find method returns index of that string and if not present returns -1 whereas in variable name returns bollean value
# To read more about methods visit python.docs