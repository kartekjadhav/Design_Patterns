from .vehicle import Vehicle

class Car(Vehicle):
    RATE = 20
    def __init__(self, licensePlate):
        super().__init__(licensePlate, 'Car')
    def calculateFare(self, hoursStayed) -> float:
        return hoursStayed * Car.RATE