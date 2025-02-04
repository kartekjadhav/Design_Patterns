from .payment import Payment

class CreditCardPayment(Payment):
    def pay(self, amount:float):
        print(f"Payment of ${amount} has been done using Credit Card")