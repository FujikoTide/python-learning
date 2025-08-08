from typing import NamedTuple


class Color(NamedTuple):
    red: int
    green: int
    blue: int


color = Color(255, 255, 255)

# color.red = 234

print(color)
