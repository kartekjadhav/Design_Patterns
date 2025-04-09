from .paymentStrategy import PaymentStrategy
class Payment:
    def processPayment(self, fare:float, paymentMethod:PaymentStrategy):
        paymentMethod.processPayment(fare)