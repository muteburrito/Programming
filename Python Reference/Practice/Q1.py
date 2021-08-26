# Read a poems.txt file and check if the word entered is in it

a = input('Enter the word you want to check: ')

with open('D:\Programming\Python Reference\Practice\poems.txt', 'r') as p:
    find = p.read().lower()
    if a in find:
        print(a + ' is present')
    else:
        print(a + ' not present')
