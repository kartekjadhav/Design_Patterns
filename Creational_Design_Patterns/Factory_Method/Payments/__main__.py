from payment_factory import PaymentFactory

factory = PaymentFactory()
obj = factory.create("PhonePePayment")
obj.pay(1000.00)