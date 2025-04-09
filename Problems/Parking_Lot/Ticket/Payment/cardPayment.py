from .paymentStrategy import PaymentStrategy

class CardPayment(PaymentStrategy):
    def processPayment(self, fare:float):
        print(f"Processed payment of {fare} Rps using Card.")