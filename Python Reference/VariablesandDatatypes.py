# Variable name should not start with number
a = "Doube"  # Here it automatically identifies which type of data is stored
b = 4.654  # most important comments are written by using hashtag
c = 15  # these values are stored in the memory and these values are stored in containers which are variables
d = 'Single'
e = '''Triple'''
# strings can be stored in three ways, as mentioned above.
# Variable names are case sensitive
# for tripple quote the string can be of multiple lines

f = '''hello
this 
is 
multi-line
'''

g = True  # this is boolean which gives true or false

h = None  # this signifies none which has no value

# printing Variables:
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)
print(h)

# each variable has its class which denotes its type. It can be given by print(type(variable_name))
# printing the types of variable:
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))
print(type(g))
print(type(h))

# We can also change the value a data type-

z = '45'
print(z)
# total = z + 1 this will give error so we can concatinate this string to int
z = int(z)
total = z + 1
print(total)
