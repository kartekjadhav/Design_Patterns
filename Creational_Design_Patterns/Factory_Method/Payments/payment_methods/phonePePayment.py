from payment_methods import Payment

class PhonePePayment(Payment):
    def pay(self, amount):
        print(f"Payment of ${amount} has been done using PhonePe")