from dataclasses import dataclass, field


@dataclass
class MovementSystem:
    def move(self, distance):
        return f"walking {distance} distance!"


@dataclass
class Battery:
    level: int = 100

    def consume(self, amount):
        return f"consuming {amount}% battery! {round(self.level, 2)} remaining!"


@dataclass
class Robot:
    _movement_system: MovementSystem = field(default_factory=MovementSystem)
    _battery: Battery = field(default_factory=Battery)

    def walk(self, distance):
        amount = round(distance * 0.1, 2)
        if self._battery.level - amount >= 0:
            self._battery.level -= amount
            print(self._movement_system.move(distance))
            print(self._battery.consume(amount))
        else:
            print("Beeeeeoooooopppp! Out of power!")


robot = Robot()
robot2 = Robot()
print(robot)
robot.walk(3)
robot.walk(6)
robot.walk(7)
robot.walk(8)
robot.walk(800)
robot.walk(800)
robot.walk(800)
print(robot)
print("=" * 50)
print(robot2)
robot2.walk(4)
robot2.walk(56)
robot2.walk(7)
robot2.walk(87)
robot2.walk(80)
robot2.walk(800)
robot2.walk(200)
print(robot2)
