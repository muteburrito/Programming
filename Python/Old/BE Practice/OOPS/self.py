class Employee:
    company = 'Google'
    def getsalary(self):# Here self acts like a function argument and accepts the object there
        print(f'Salary is {self.salary}')
#         print('Salary is 100k')

# 
# emp1 = Employee()
# emp1.name = 'CK'
# emp1.salary()
emp2 = Employee()
emp2.salary = 100000
emp2.getsalary()

