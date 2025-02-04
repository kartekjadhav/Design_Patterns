from .payment import Payment

class GooglePayPayment(Payment):
    def pay(self, amount:float):
        print(f"Payment of ${amount} has been done using Google Pay")