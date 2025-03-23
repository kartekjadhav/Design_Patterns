from .PaymentMethod import PaymentMethod

class PaymentProcessor():
    def processPayment(self, paymentType:PaymentMethod, amount:float):
        if amount > 0:
            paymentType.processPayment(amount)