# Created a set:
b = set()

# To add elements in a set:
b.add(4)
b.add(5)
print(b)
print(type(b))

# Cannot add list in a set as list is hasable
# So, hashable is a feature of Python objects that tells if the object has a hash value or not.
#  If the object has a hash value then it can be used as a key for a dictionary or as an element in a set. 
# An object is hashable if it has a hash value that does not change during its entire lifetime.
# As list can be modified so list cannot be added but in that case tuple can be added in a set. 
# Hence Dictionary also cannot be added

b.add((3,5,6,7))
print(b)

# In simple words we cannot add any element which can be modified during its entire lifespan

print(len(b)) # This will print the length of b set

b.remove(5) # This will remove the element entered in the parenthisis
print(b)

# To remove any random element from the set we use pop method and print it in return
print(b.pop())

# To clear out a set and make it empty we use :
b.clear()
print(b)

# We also have intersection method which will return a new set containing common elements of 2 sets:
s1 = {1,3,5,7}
s2 = {2,5,9,4}
print(s1.intersection(s2))
# In the above example we can define a new set in the parethisis also like this:
print(s1.intersection({1,7,11,45}))

# Similarly we have union which will give a new set with elements from all sets combined together:
print(s1.union(s2))
# Similar to intersection we can define a set in parethisis:
print(s1.union({6,8}, s2)) # Also we can make a union of more sets also

# We can store union and intersection of sets in other set also.
s_union = s1.union(s2, {6,8})
s_intersection = s1.intersection({1,4,7,9})
print(s_union, s_intersection)
