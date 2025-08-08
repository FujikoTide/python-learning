from typing import List


class Student:
    def __init__(self, name: str, student_id: int):
        self.name = name
        self.student_id = student_id
        self._grades: List[int] = []

    def __repr__(self):
        return f"Student(name={self.name}, student_id={self.student_id}, grades={self._grades[:3]})"

    def add_grade(self, grade: int):
        if not (0 <= grade <= 100):
            raise ValueError("Grade must be between 0 and 100")
        self._grades.append(grade)

    def get_average_grade(self) -> float:
        if not self._grades:
            raise ValueError(
                f"Cannot calculate an average grade. No grades associated with {self.name}"
            )
        average_grade = sum(self._grades) / len(self._grades)
        return round(average_grade, 2)


harold = Student("Harold", 222)
print(harold)
# print(harold.get_average_grade())
# harold.add_grade(-4)
# harold.add_grade(199)
harold.add_grade(55)
harold.add_grade(99)
harold.add_grade(71)
harold.add_grade(66)
print(harold.get_average_grade())
print(harold)
