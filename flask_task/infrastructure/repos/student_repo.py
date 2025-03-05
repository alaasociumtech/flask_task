from flask_task.domain.student import Student
from flask_task.infrastructure.repos.base_repo import BaseRepo


class StudentRepo(BaseRepo[Student]):
    def __init__(self) -> None:
        super().__init__(Student)
