from .bike import Bike 

class Audi_Bike(Bike):
    def startBike(self):
        print(f"{__class__.__name__} is starting...")
        print(f"{__class__.__name__} is started")
    
    def accelarateBike(self):
        print(f"{__class__.__name__} is accelarating...")