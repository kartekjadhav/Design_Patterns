from .car import Car

class BMW_Car(Car):
    def startCar(self):
        print(f"{__class__.__name__} is starting...")
        print(f"{__class__.__name__} is started")
    
    def accelarateCar(self):
        print(f"{__class__.__name__} is accelarating...")