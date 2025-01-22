from milkshake_factory import MilkshakeFactory

factory = MilkshakeFactory()
shake = input("Enter the shake you want -> ")
myshake = factory.get(shake)
myshake.createShake()