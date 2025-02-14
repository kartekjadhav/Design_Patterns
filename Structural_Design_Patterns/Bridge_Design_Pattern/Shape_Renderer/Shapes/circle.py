from .shape import Shape

class Circle(Shape):
    def __init__(self, renderer):
        super().__init__(renderer)
        self._radius = int(input("Enter value of radius: ").strip())
    
    def area(self):
        print(f"Area is {3.14*self._radius*self._radius}")
    
    def draw(self):
        self._renderer.renderCircle()