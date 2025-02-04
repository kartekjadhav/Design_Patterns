from .payment import Payment

class PaypalPayment(Payment):
    def pay(self, amount:float):
        print(f"Payment of ${amount} has been done using Paypal")