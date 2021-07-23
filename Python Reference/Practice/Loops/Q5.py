# To check if a number is prime or not:

a = int(input('Enter the number: '))

prime = True

for i in range(2,a):
    if (a % i) == 0:
        prime = False
        break

if prime == True:
    print(f'{a} is a Prime number')
else:
    print(f'{a} is not a Prime number')