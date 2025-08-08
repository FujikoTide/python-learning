from dataclasses import dataclass


@dataclass
class Person:
    name: str


@dataclass
class Artist(Person):
    def create_art(self):
        return "Here's some art !"


@dataclass
class Musician(Person):
    def play_instrument(self):
        return "beep boop"


@dataclass
class Performer(Artist, Musician):
    def stage_performance(self):
        create_art = super().create_art()
        play_instrument = super().play_instrument()
        return f"{create_art}\n{play_instrument}"


performer = Performer("Harold")
print(performer)
print(performer.stage_performance())
