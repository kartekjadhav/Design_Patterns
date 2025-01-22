import threading

class Singleton:
    __instance = None
    __lock = threading.Lock()
    def __new__(cls):
        if cls.__instance == None:
            with cls.__lock:
                if cls.__instance == None:
                    cls.__instance = super().__new__(cls)
        return cls.__instance

s1 = Singleton()
s2 = Singleton()
s3 = Singleton()    
print(s1, s2, s3)