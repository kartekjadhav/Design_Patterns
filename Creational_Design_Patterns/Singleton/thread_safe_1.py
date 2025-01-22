import threading

class Singleton:
    __instance = None
    __lock = threading.Lock()
    def __init__(self):
        if Singleton.__instance is None:
            Singleton.__instance = self
        else:
            raise Exception("Cannot create more than one object")    
    
    @staticmethod
    def getInstance():
        if Singleton.__instance is None:
            with Singleton.__lock:
                if Singleton.__instance is None:
                    Singleton()
        return Singleton.__instance

s1 = Singleton.getInstance()
s2 = Singleton.getInstance()

print(s1)
print(s2)