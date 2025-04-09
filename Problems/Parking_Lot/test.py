class Car:
    def __init__(self):
        pass

class Bike:
    def __init__(self):
        pass

a = 'car'
car = Car()
b = car.__class__.__name__
print(a.lower() == b.lower())