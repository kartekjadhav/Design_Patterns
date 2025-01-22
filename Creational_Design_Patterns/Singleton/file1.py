import random

class Singleton:
    __instance = None

    def __init__(self):
        if Singleton.__instance == None:
            self.connectionId = random.random()
            Singleton.__instance = self
        else:
            raise Exception("Cannot create more than one object")
    @staticmethod
    def getInstance():
        if Singleton.__instance == None:
            Singleton()
        return Singleton.__instance
    
    def getData(self):
        print(self.connectionId)

s1 = Singleton.getInstance()
s2 = Singleton.getInstance()
s1.getData()
s2.getData()
print(f"s1 - {s1}")
print(f"s2 - {s2}")
s3 = Singleton()
