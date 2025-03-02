from typing import Any

from flask_task.domain.student import Student
from flask_task.infrastructure.base_repo import BaseRepo


class StudentRepo(BaseRepo[Student]):
    def add_student(self, name: str, age: int, grade: str) -> Any:
        student = Student(self.counter, name, age, grade)
        return self.create(student)
