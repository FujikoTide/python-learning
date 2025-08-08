from dataclasses import dataclass


@dataclass
class Animal:
    def move(self) -> str:
        return "Animal moves"


@dataclass
class Mammal(Animal):
    def move(self) -> str:
        return "Mammal walks on land"


animal = Animal()
mammal = Mammal()

print(animal.move())
print(mammal.move())
