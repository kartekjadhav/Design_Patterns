from .shape import Shape

class Square(Shape):
    def __init__(self, renderer):
        super().__init__(renderer)
        self._side = int(input("Enter value of side: ").strip())
    
    def area(self):
        print(f"Area is {self._side**2}")
    
    def draw(self):
        self._renderer.renderSquare()