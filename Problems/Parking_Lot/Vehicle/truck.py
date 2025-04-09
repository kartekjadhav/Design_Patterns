from .vehicle import Vehicle

class Truck(Vehicle):
    RATE = 30
    def __init__(self, licensePlate):
        super().__init__(licensePlate, 'Truck')
    def calculateFare(self, hoursStayed) -> float:
        return hoursStayed * Truck.RATE