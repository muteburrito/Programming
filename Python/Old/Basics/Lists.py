# Python list are containers in which we can store values in it. They are ordered

a = [12, 4 ,6 ,12 ,43]
print(a)
b = [] # This is a empty list
c = [1,] # This creates a list with only 1 element 
# c[1] = 34 # This will give error 
print(c)
print(b)
# Lists are always defined in square brackets
# Similar to strings here also we have indexing
print(a[0])
# Indexing starts from 0
print(a[-1])
# We can also modify the list in the following manner :
a[2] = 44
print(a)
# We can create list of items of different types
types = [44, 'asas', 5.7, True]
print(types)

#list slicing
frnds = ["Tom", "Tim", "Rakesh", "Albert"]
print(frnds[0:4])
# Slicing in lists is exactly same as string slicing