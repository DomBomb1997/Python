from abc import ABC, abstractmethod
class car(ABC):
    def payslip(self, amount):
        print("Your purchase amount: ",amount)
#this function is telling us to pass in an argument, but we won't tell you how or what kind
#of data it will be.
        @abstractmethod
        def payment(self, amount):
            pass
class DebitCardPayment(Car):
#there we've defined how to implement the patyment function from its parent payslip class.
    def payment(self, amount):
        print("Your purchase amount of () exceeded your $100 limit".format(amount))

onj = DebitCardPayment()
onj.payslip("$400")
onj.payment("$400")
