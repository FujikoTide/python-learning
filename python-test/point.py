class Point:
    def __init__(self, x, y):
        object.__setattr__(self, "x", x)
        object.__setattr__(self, "y", y)

    def __setattr__(self, name, value):
        raise AttributeError("Cannot modify attributes of immutable object")


point = Point(3, 5)

print(point)
print(point.x)
print(point.y)

point.x = 7
