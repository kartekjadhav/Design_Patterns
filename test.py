import threading
from abc import ABC, abstractmethod
from copy import deepcopy

class Prototype(ABC):
    @abstractmethod
    def clone(self):
        pass

class Singleton(ABC):
    __obj = None
    __lock = threading.Lock()
    def __init__(self):
        if not Singleton.__obj:
            Singleton.__obj = self
        else:
            raise Exception("Only one object can be created")
    
    @staticmethod
    def getObj():
        if not Singleton.__obj:
            with Singleton.__lock:
                if not Singleton.__obj:
                    Singleton()
        return Singleton.__obj
    
    def clone(self):
        raise Exception("Cant clone the object as this class is Singleton")

obj1 = Singleton.getObj()
print(f"obj1 - {id(obj1)}")
obj2 = Singleton.getObj()
print(f"obj2 - {id(obj2)}")
obj3 = obj1.clone()
print(f"obj3 - {id(obj3)}")