# Write a program to compare 4 numbers entered by the user and display the greatest one

a = int(input('Enter number 1: '))
b = int(input('Enter number 2: '))
c = int(input('Enter number 3: '))
d = int(input('Enter number 4: '))

if (a > b):
    g1 = a
else:
    g1 = b

if (c > d):
    g2 = c
else:
    g2 = d

if (g1 > g2):
    print(g1, 'is greatest')
else:
    print(g2, 'is greatest')
