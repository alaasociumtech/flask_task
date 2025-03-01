from domain.student import Student

from .base_repo import BaseRepo


class StudentRepo(BaseRepo[Student]):
    def add_student(self, name: str, age: int, grade: str) -> Student | None:
        student = Student(self.counter, name, age, grade)
        return self.create(student)
