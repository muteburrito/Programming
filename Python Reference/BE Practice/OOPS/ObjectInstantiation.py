class Form():
    def printdata(self):
        print(self.name, self.address)

# object is nothing but a variable:

user1_form = Form()
user1_form.name = 'CK'
user1_form.address = 'Pune'
user1_form.printdata()
