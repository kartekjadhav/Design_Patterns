from .cardPayment import CardPayment
from .upiPayment import UPIPayment
from .cashPayment import CashPayment
from .payment import Payment
class PaymentService:
    def processPayment(self, fare:float):
        print(f"Total Fees: {fare}")
        print(f"Choose your preffered payment method serial number -> ")
        print(f"1. Cash Payment")
        print(f"2. UPI Payment")
        print(f"3. Card Payment")
        userChoice = int(input())
        payment = Payment()

        match userChoice:
            case 1:
                payment.processPayment(fare, CashPayment())
            case 2:
                payment.processPayment(fare, UPIPayment())
            case 3:
                payment.processPayment(fare, CardPayment())
            case _:
                print("Invalid payment selection, processing with default payment method CashPayment")
                payment.processPayment(fare, CashPayment())