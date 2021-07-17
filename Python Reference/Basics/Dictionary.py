# Dictionary is a collection of key value pairs, also it is unordered. Its is also modifiable
#keys can be used in upper and lower case also
MyDict = {
    "Fast" : "Speed",
    "Run" : "Action",
    "Marks" : [1,4,7,8],
    "newdict" : {"Command" : "Input"}
}
# A dictionary must start with curly braces. It is nothing but collection of key and a value associated to that key
print(MyDict["Run"]) # This will give the definition of the key or the value of that key
# Key and value can be of any data type, even list and tuple and even another dictionary 
print(MyDict["Marks"])
print(MyDict["newdict"])

# Below is an example of Nested Dictionary
print(MyDict["newdict"]["Command"]) # this will print the value of the dictionary inside our base dictionary 

# Modifying dictionary:
MyDict["Fast"] = 'Hello'
print(MyDict["Fast"]) # In a similar way we can also update list and tuples and dictionary inside a dictionary
# Keys are unique 

