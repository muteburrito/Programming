# Factorial of a number

a = int(input('Enter the number you want factorial of: '))

i = 1
for j in range(2,a+1):
    i = i * j
print(f'Factorial of the the number is {i}')