from .paymentStrategy import PaymentStrategy

class UPIPayment(PaymentStrategy):
    def processPayment(self, fare:float):
        print(f"Processed payment of {fare} Rps using UPI.")