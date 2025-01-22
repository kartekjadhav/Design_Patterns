class Singleton:
    __instance = None

    def __new__(cls):
        if cls.__instance == None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

s1 = Singleton()
s2 = Singleton()
print(s1)
print(s2)