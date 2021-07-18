# Continue is used to skip some value, like this 

for i in range(1,10):
    if i < 5:
        continue # This will run the loop till this this line and not run the print line until it gets the condition false
    # So here 5 and above numbers will be printed 
    print(i)

# This is useful when we want to print even numbers we can use i % 2 in if condition