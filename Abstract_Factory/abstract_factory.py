from inspect import isclass, isabstract, getmembers
import vehichle_factories

class AbstractFactory():
    factories = {}
    def __init__(self):
        self.create()
    def create(self):
        implementations = getmembers(vehichle_factories, lambda m: isclass(m) and not isabstract(m) and issubclass(m, vehichle_factories.VehicleFactory))
        for key, value in implementations:
            self.factories[key] = value
    def getFactory(self, brand):
        if brand in self.factories:
            return self.factories[brand]()
        else:
            raise ValueError(f"We dont support {brand} yet!")
