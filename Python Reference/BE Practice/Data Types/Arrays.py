# Creating Arrays:

import array as arr

a1 = arr.array('i', [1,2,3])
print('The array is: ')
for i in range (0,3):
    print(a1[i])
print(type(a1))
