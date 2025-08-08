from dataclasses import dataclass


@dataclass
class Shape:
    def area(self) -> str:
        return "this has an area !"


@dataclass
class Circle(Shape):
    def area(self) -> str:
        return "this is a circle area !"


@dataclass
class Rectangle(Shape):
    def area(self) -> str:
        return "this is a rectangle area !"


@dataclass
class ProcessShapes:
    shapes: Shape | Circle | Rectangle


shape = Shape()
circle = Circle()
rectangle = Rectangle()

shapes_list = [
    ProcessShapes(shapes=shape),
    ProcessShapes(shapes=circle),
    ProcessShapes(shapes=rectangle),
]


def printShapes(shapes_list: list[ProcessShapes]):
    for shape in shapes_list:
        print(shape.shapes.area())


printShapes(shapes_list)
