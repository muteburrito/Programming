# This is a kind of loop which runs until the condition is true
i = 0
while i < 5:
    print(i)
    i = i + 1 # This line is important as if this is not there the loop will run in an infinite sequence
# Here once the condition ie. i < 5 becomes true the loop will stop

# We can also use data from a list:

fruits = ['Banana', 'Mango', 'Apple', 'Watermelon']

i = 0
while i < len(fruits):
    print(fruits[i])
    i = i + 1