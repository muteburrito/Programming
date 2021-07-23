# Recursion is a function which calls itself using mathematical beauty
# eg: Lets consier the problem of the factorial
# Normal method using function
## def factorial(number = 1):
##     product = 1 
##     for i in range(1,number):
##         product = product * i
##     print(product)
## 
## a = input('Enter the number: ')
## print(factorial(a))

# To find factorial of n we can use 1 * 2 * 3 *.... * n-1 * n
# so this can be formulated as :
# (n-1)! * n we can use this formula to create a function calling it self


def factorial_recursive(number):
    if number == 1 or number == 0: # Base condition of a recursion
        return 1
    else:
        return number * factorial_recursive(number-1)

a = int(input('Enter number: '))
f = factorial_recursive(a)
print(f)

# The programmer needs to be extremely careful while working with recursions to ensure that the function does not calls it self again and again 
# Recursion can be refereed as loops of function which needs a base condition to run successfully 
# Recursion is the best way to code an algorithm directly 