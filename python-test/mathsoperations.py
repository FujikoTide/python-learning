class MathsOperations:
    @staticmethod
    def add(a: float, b: float) -> float:
        return a + b

    @staticmethod
    def subtract(a: float, b: float) -> float:
        return a - b

    @staticmethod
    def multiply(a: float, b: float) -> float:
        return a * b

    @staticmethod
    def divide(a: float, b: float) -> float:
        return a / b


print(MathsOperations.add(3, 6))
print(MathsOperations.subtract(7, 3))
print(MathsOperations.multiply(4, 8))
print(MathsOperations.divide(3, 9))
