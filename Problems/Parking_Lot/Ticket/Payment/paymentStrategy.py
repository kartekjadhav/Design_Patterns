from abc import ABC, abstractmethod

class PaymentStrategy(ABC):
    @abstractmethod
    def processPayment(self, fare:float):
        pass