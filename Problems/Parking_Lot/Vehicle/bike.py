from .vehicle import Vehicle

class Bike(Vehicle):
    RATE = 10
    def __init__(self, licensePlate):
        super().__init__(licensePlate, 'Bike')
    def calculateFare(self, hoursStayed) -> float:
        return hoursStayed * Bike.RATE