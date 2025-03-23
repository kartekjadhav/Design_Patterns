from .PaymentMethod import PaymentMethod

class UPIPayment(PaymentMethod):
    def processPayment(self, amount:float):
        print(f"Processing payment of {amount} Rupees by UPI")