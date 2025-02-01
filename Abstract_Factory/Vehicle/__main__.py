from abstract_factory import AbstractFactory

brand = input("Enter the factory you want to access -> ")
obj = AbstractFactory()
factory = obj.getFactory(brand)
car = factory.createCar()
car.startCar()
car.accelarateCar()

bike = factory.createBike()