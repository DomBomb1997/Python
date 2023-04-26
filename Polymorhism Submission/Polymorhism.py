#parent class user
class User:
    name = 'Mark'
    email = 'mark@gmail.com'
    password = '123abc'

    def getLoginInfo(self):
        entry_name = input("Enter your name: ")
        entry_email = input("Enter your email: ")
        entry_password = input("Enter your password: ")
        if (entry_email == self.email and entry_password == self.password):
            print("Welcome back, {}!".format(entry_name))
        else:
            print("The password or email is incorrect.")

#Child Class Employee
class Employee(User):
    base_pay = 18.00
    department = "General"
    pin_number = "3990"


#This is the same method in the parent class "User".
#The difference is that, instead of using entry_password, we're using entry pin.

    def getLoginInfo(self):
        entry_name = input("Enter your name: ")
        entry_email = input("Enter your email: ")
        entry_pin = input("Enter your pin: ")
        if (entry_email == self.email and entry_pin == self.pin_number):
            print("Welcome back, {}!".format(entry_name))
        else:
            print("The pin or email is incorrect.")

#My own class
class Person(person):
    name = "Jake"
    Phone = "1234567890"
    cc = "0987654321"


#This is the same method in the parent class "User".
    def getLoginInfo(self):
        entry_name = input("Enter your name: ")
        entry_phone = input("Enter your phone number: ")
        entry_cc = input("Enter your cc number: ")
        if (entry_name == self.name and entry_phone == self.phone):
            print("Welcome back, {}!".format(entry_name))
        else:
            print("Phone or cc is incorrect.")

#The following code invokes the methods inside each class for the user and employee.

customer = User()
customer.getLoginInfo()

manger = Employee()
manger.getLoginInfo()

person = Person()
person.getLoginInfo()




