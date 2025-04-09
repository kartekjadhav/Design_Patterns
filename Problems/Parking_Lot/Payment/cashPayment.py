from .paymentStrategy import PaymentStrategy

class CashPayment(PaymentStrategy):
    def processPayment(self, fare:float):
        print(f"Processed payment of {fare} Rps using Cash.")