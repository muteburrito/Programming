# whenever we type anything in a input it is treated as a string even s number
## year = input("Enter your Birth year: ")
# print(type(year))
# here int function will try to convert that string to int
# We have one more function called type() which returns the type of variable or data
## age = 2021 - int(year)
# print(age)
# print(type(age))

# Now lets take a example:

pounds = input('Enter your weight in pounds: ')
kg = int(pounds) * 0.453592
print(kg)
