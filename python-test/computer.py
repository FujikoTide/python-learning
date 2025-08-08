from dataclasses import dataclass


@dataclass
class CPU:
    model: str
    speed: int


@dataclass
class RAM:
    model: str
    speed: int
    size: int


@dataclass
class Storage:
    model: str
    capacity: int


@dataclass
class Computer:
    cpu: CPU
    ram: RAM
    storage: Storage

    def get_specs(self):
        return f"CPU: {self.cpu}, RAM: {self.ram}, Storage: {self.storage}"


cpu1 = CPU("Ryzen 5", 3500)
cpu2 = CPU("Ryzen 7", 4500)
cpu3 = CPU("Ryzen 9", 5500)

ram1 = RAM("Basic", 3000, 8)
ram2 = RAM("Good", 3200, 16)
ram3 = RAM("Super", 3600, 32)

storage1 = Storage("Small", 256)
storage2 = Storage("Medium", 1000)
storage3 = Storage("Large", 2000)

computer1 = Computer(cpu1, ram1, storage1)
computer2 = Computer(cpu2, ram2, storage2)
computer3 = Computer(cpu3, ram3, storage3)

print(computer1.get_specs())
print(computer2.get_specs())
print(computer3.get_specs())
