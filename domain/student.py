from domain.base_entity import BaseEntity


class Student(BaseEntity):
    def __init__(self, student_id: int, name: str, age: int, grade: str):
        super().__init__(student_id)
        self.name = name
        self.age = age
        self.grade = grade

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "age": self.age,
            "grade": self.grade
        }
