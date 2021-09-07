# Special method __init__ is always executed automatically even if that function is not called

class Employee():
    name = 'Google'

    def __init__(self, name, salary, dept): # This will be used when an object is instanciated
        print(f'You are {name}, you work in {dept} and your salary is {salary}')

emp1 = Employee('CK', 100000, 'YouTube')

# So basically a constructor is called even if the user does not call it.