from dataclasses import dataclass


@dataclass
class Shape:
    color: str

    def describe(self):
        return f"A shape of color {self.color}"


@dataclass
class Circle(Shape):
    radius: float

    def describe(self):
        parent_description = super().describe()
        return f"{parent_description}, radius {self.radius}"


circle = Circle("green", 5)
print(circle)
print(circle.describe())
