class Form():
    def printdata(self):
        print(self.name, self.address)

# object is nothing but a variable:

user1_form = Form() # Here an object user1_form is instanciated/created which uses data from class Form
user1_form.name = 'CK'
user1_form.address = 'Pune'
user1_form.printdata()
