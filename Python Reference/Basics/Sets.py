# Set start with curly braces. It is a collection of non repetitive elements. 
# They are unordered and not indexed

a = {2,4,7,1,9,4} # Here as I said 1 which is repetated will not be printed 
print(type(a))
print(a)

# Empty set:
b = set()
print(type(b))
# If we ave a set with lets say 20 and 20.0 then it will be considered s same and only 20 will be printed but if we have "20" as a string then ot will be considered different