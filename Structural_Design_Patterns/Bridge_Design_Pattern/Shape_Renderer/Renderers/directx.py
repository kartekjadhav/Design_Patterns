from .renderer import Renderer

class DirectX(Renderer):
    def renderCircle(self):
        print(f"Rendering Circle...")
        print(f"Circle has been rendered --> O O O . copyright{self.__class__.__name__}")
    def renderSquare(self):
        print(f"Rendering Square...")
        print(f"Square has been rendered --> [] [] [] . copyright{self.__class__.__name__}")
    def renderTriangle(self):
        print(f"Rendering Triangle...")
        print(f"Triangle has been rendered --> A A A . copyright{self.__class__.__name__}")