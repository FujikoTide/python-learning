from dataclasses import dataclass
from multiprocessing import Value
from typing import Optional


@dataclass
class Dog:
    name: str

    def make_sound(self):
        return "Woof!"


@dataclass
class Cat:
    name: str

    def make_sound(self):
        return "Meow!"


@dataclass
class Duck:
    name: str

    def make_sound(self):
        return "Quack!"


class AnimalFactory:
    @staticmethod
    def create_animal(type: str, name: str) -> Dog | Cat | Duck:
        type = type.lower()
        if type == "dog":
            return Dog(name)
        elif type == "cat":
            return Cat(name)
        elif type == "duck":
            return Duck(name)
        else:
            raise ValueError(f"Unknown animal of type: {type}")


def animal_parade(animals):
    for animal in animals:
        print(animal.make_sound())


dog = AnimalFactory().create_animal("Dog", "Harold")
cat = AnimalFactory().create_animal("cat", "George")
duck = AnimalFactory().create_animal("duck", "Oswald")


animals = [dog, cat, duck]
animal_parade(animals)
