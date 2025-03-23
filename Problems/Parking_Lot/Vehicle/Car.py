from .Vehicle import Vehicle

class Car(Vehicle):
    RATE = 10
    def __init__(self, licensePlate):
        super().__init__(licensePlate, 'Car')
    
    def calculateFare(hoursParked: float):
        return hoursParked * Car.RATE
