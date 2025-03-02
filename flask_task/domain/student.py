from dataclasses import dataclass
from typing import Any

from flask_task.domain.base_entity import BaseEntity


@dataclass
class Student(BaseEntity):
    name: str
    age: int
    grade: str

    def to_dict(self) -> dict[str, Any]:
        return {
            'id': self.id,
            'name': self.name,
            'age': self.age,
            'grade': self.grade
        }
