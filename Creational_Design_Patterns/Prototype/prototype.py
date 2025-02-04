from abc import ABC, abstractmethod
from copy import deepcopy

class Prototype(ABC):
    @abstractmethod
    def clone(self):
        pass

class ConcretePrototype1(Prototype):
    def __init__(self, name, value):
        self.name = name
        self.value = value
    
    def __repr__(self):
        return f"ConcretePrototype1(name={self.name}, value={self.value})";

    def clone(self):
        return deepcopy(self)

original = ConcretePrototype1("Kartek", "25");
cloned = original.clone()

print(original)
print(cloned)

cloned.name = "Sid"
cloned.value = 23

print(original)
print(cloned)