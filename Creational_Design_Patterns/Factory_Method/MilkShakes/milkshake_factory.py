from inspect import isclass, isabstract, getmembers
import milkshake_types

class MilkshakeFactory():
    milkshake_implementations = {}
    def __init__(self):
        self.create()

    def create(self):
        implementations = getmembers(milkshake_types, lambda m: isclass(m) and not isabstract(m) and issubclass(m, milkshake_types.Milkshake))
        for key, value in implementations:
            self.milkshake_implementations[key] = value
    def get(self, shake):
        if shake in self.milkshake_implementations:
            return self.milkshake_implementations[shake]()
        else:
            raise ValueError(f"We dont serve ${shake} yet!")
