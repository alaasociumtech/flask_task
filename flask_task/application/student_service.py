from typing import Any

from flask_task.application.base_service import BaseService
from flask_task.domain.student import Student
from flask_task.infrastructure.repos.student_repo import StudentRepo
from flask_task.infrastructure.repos.unit_of_work import UnitOfWork


class StudentService(BaseService):
    def __init__(self, uow: UnitOfWork):
        super().__init__(uow)
        self.student_repo = StudentRepo()

    def add_student(self, name: str, age: int, grade: str) -> Student:
        student = Student(id=0, name=name, age=age, grade=grade)
        created_student = self.student_repo.create(student)
        self.uow.commit()
        return created_student

    def get_student(self, student_id: int) -> Any:
        return self.student_repo.get_entity_by_id(student_id)

    def update_student(self, student_id: int, name: str, age: int, grade: str) -> Any:
        student = self.student_repo.get_entity_by_id(student_id)
        if not student:
            return None
        student.name = name
        student.age = age
        student.grade = grade
        updated_student = self.student_repo.update(student_id, student)
        self.uow.commit()
        return updated_student

    def delete_student(self, student_id: int) -> Any:
        deleted_student = self.student_repo.delete(student_id)
        self.uow.commit()
        return deleted_student
