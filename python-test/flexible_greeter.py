from dataclasses import dataclass


@dataclass
class Greeter:
    def greet(self, name="Guest", formality="casual"):
        if formality == "casual":
            return f"Hi, {name}!"
        elif formality == "formal":
            return f"Good day, {name}."


greeter = Greeter()

print(greeter.greet())
print(greeter.greet(name="Harold"))
print(greeter.greet(name="Harold", formality="casual"))
print(greeter.greet(name="Harold", formality="formal"))
print(greeter.greet(formality="casual"))
print(greeter.greet(formality="formal"))
