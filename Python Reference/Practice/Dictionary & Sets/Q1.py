# Create a Dictionary to accept a user option and give its hindi to english translation

myDict = {'Pankha' : 'Fan',
'Dabba' : 'Box',
'Vastu' : 'Item'
}
print('Options are: ', myDict.keys())
a = input('Enter your option: \n')
print('The translation of your hindi word is: ', myDict.get(a)) 
# As we know .get methond will return none if the key is not present in the dictionary