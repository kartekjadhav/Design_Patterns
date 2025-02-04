from inspect import isclass, isabstract, getmembers
import payment_methods

class PaymentFactory:
    payment_implementations = {}
    def __init__(self):
        self.loadPayments()
    def loadPayments(self):
        implementations = getmembers(payment_methods, lambda m: isclass(m) and not isabstract(m))
        for key, value in implementations:
            if issubclass(value, payment_methods.Payment):
                self.payment_implementations[key] = value
    
    def create(self, method: str):
        if method in self.payment_implementations:
            return self.payment_implementations[method]()
        else:
            raise ValueError(f"{method} is currently not supported")