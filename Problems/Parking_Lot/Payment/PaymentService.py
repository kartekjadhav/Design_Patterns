from .CashPayment import CashPayment
from .CreditCardPayment import CreditCardPayment
from .UPIPayment import UPIPayment
from .PaymentProcessor import PaymentProcessor

class PaymentService():
    
    def __init__(self):
        self.paymentProcessor = PaymentProcessor()

    def initiatePayment(self, amount: float):
        print("Press the respective serial number to process payment - ")
        print("1. UPI")
        print("2. Credit Card")
        print("3. Cash")
        ip = int(input().strip())

        match ip:
            case 1:
                self.paymentProcessor.processPayment(UPIPayment(), amount)
            case 2:
                self.paymentProcessor.processPayment(CreditCardPayment(), amount)
            case 3:
                self.paymentProcessor.processPayment(CashPayment(), amount)
            case _:
                print("Invalid payment choice. Processing payment by Cash by default")
                self.paymentProcessor.processPayment(CashPayment(), amount)
