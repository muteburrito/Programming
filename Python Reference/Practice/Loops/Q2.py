# To create a multiplication table of a given number

number = int(input('Enter the number you want table of: '))

i = 1
for i in range(1,11):
    print(f'{number} x {i} = {number * i}')
    i += 1

