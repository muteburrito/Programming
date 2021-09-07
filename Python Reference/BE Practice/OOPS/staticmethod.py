# if we use static method then we dont need self argument

from datetime import datetime

class Routine:
    type = 'Daily'

    def getsalary(self, signature):
        print(f'Salary is {self.salary}\n {signature}')

    @staticmethod # This is how we define a static method
    def greetusr():
        print('Good Morning')
    
    @staticmethod
    def timeprint():
        time = datetime.today()
        print(f'The current time is {time}')

emp1 = Routine()
emp1.greetusr()
emp1.salary = 50000
emp1.getsalary('Chinmay')
emp1.timeprint()