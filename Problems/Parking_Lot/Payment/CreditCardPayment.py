from .PaymentMethod import PaymentMethod

class CreditCardPayment(PaymentMethod):
    def processPayment(self, amount:float):
        print(f"Processing payment of {amount} Rupees by Credit Card")