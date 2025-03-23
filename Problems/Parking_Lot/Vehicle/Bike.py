from .Vehicle import Vehicle

class Bike(Vehicle):
    RATE = 5
    def __init__(self, licensePlate):
        super().__init__(licensePlate, 'Bike')
    
    def calculateFare(hoursParked: float):
        return hoursParked * Bike.RATE
