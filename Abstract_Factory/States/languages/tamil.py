from language import Language

class Tamil(Language):
    def greet(self):
        print(f"In {__class__.__name__} we greet as 'Vannakam!'")