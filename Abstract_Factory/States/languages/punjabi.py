from language import Language

class Punjabi(Language):
    def greet(self):
        print(f"In {__class__.__name__} we greet as 'Sat Sriakal!'")