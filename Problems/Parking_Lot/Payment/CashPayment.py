from .PaymentMethod import PaymentMethod

class CashPayment(PaymentMethod):
    def processPayment(self, amount:float):
        print(f"Processing payment of {amount} Rupees by Cash")