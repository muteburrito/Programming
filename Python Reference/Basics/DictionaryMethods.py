MyDict = {
    "Fast" : "Speed",
    "Run" : "Action",
    "Marks" : [1,4,7,8],
    "newdict" : {"Command" : "Input"},
    1 : 34
}

print(list(MyDict.keys())) # This will return the keys in our dictionary in a list format
print(MyDict.values())
print(MyDict.items()) # This wil print the content of the dictionary to make it easy to iterate

update = {
    'Galaxy' : 'Space'
}
MyDict.update(update) # This will add the new data type in the form of key value pair in the dictionary
print(MyDict)

# Now to display key values we can use .get method also
print(MyDict.get('Galaxy2')) # This will return none
# This will not throw any error while just using the square bracket with syntax :
# print(MyDict[Galaxy2]) will throw error
