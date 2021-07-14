# So combining two strings with special values is good. eg-
first = 'Jon'
last = 'Smith'

message = first + ' [' + last + ']' + ' is a coder'
# The above concatination makes the code and the string more complicated so we use formatted strings

# Formatted string is started with f and quotes
# prefix f and curly braces to insert that variable
mssg = f'{first} [{last}] is a coder'
# print(mssg)
# So all n all thse strings makes life more easier

First_Name = input("Enter your First name: ")
Last_Name = input('Enter your Last Name: ')

greeting = f'Hello {First_Name} {Last_Name}, have a wonderful day! '

print(greeting)
