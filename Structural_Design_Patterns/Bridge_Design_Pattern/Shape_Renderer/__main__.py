import Shapes
import Renderers
from inspect import isclass, getmembers, isabstract

shapes_members = getmembers(Shapes, lambda m: isclass(m) and not isabstract(m) and issubclass(m, Shapes.Shape)) 
renderer_members = getmembers(Renderers, lambda m: isclass(m) and not isabstract(m) and issubclass(m, Renderers.Renderer))

shapes = {key:value for key, value in shapes_members}
renderers = {key:value for key, value in renderer_members}

while True:
    try:
        print(f"Rendering softwares available ->")
        for key in renderers.keys():
            print(key)
        rchoice = input("Enter the rendering software you want from above: ")
        renderer = renderers[rchoice]()
        print(f"Shapes available ->")
        for key in shapes.keys():
            print(key)
        schoice = input("Enter the shape you want to draw from above: ")
        shape = shapes[schoice](renderer)
        shape.draw()
    except Exception as e:
        print(e)