from language import Language

class Marathi(Language):
    def greet(self):
        print(f"In {__class__.__name__} we greet as 'Namaste!'")