from typing import Any, Generic, List, Optional, Protocol, Type, TypeVar

from sqlalchemy.engine import Row
from sqlalchemy.orm import Session

from flask_task.infrastructure.database.connection import engine
from flask_task.infrastructure.database.schema import students


class StudentEntityProtocol(Protocol):
    id: int
    name: str
    age: int
    grade: str


E = TypeVar('E', bound=StudentEntityProtocol)


def row_to_dict(row: Row[Any]) -> dict[str, Any]:
    return dict(row._mapping)


class BaseRepo(Generic[E]):
    def __init__(self, entity_type: Type[E]) -> None:
        self.entity_type = entity_type

    def get_all(self) -> List[E]:
        with Session(engine) as session:
            result = session.execute(students.select()).fetchall()
            return [self.entity_type(**row_to_dict(row)) for row in result]

    def get_entity_by_id(self, entity_id: int) -> Optional[E]:
        with Session(engine) as session:
            result = session.execute(students.select().where(students.c.id == entity_id)).first()
            return self.entity_type(**row_to_dict(result)) if result else None

    def create(self, entity: E) -> E:
        with Session(engine) as session:
            result = session.execute(
                students.insert()
                .values(name=entity.name, age=entity.age, grade=entity.grade)
                .returning(students.c.id)
            )
            session.commit()
            entity.id = result.scalar() or 0
            return entity

    def update(self, entity_id: int, updated_entity: E) -> Optional[E]:
        with Session(engine) as session:
            session.execute(
                students.update()
                .where(students.c.id == entity_id)
                .values(name=updated_entity.name, age=updated_entity.age, grade=updated_entity.grade)
            )
            session.commit()
            return self.get_entity_by_id(entity_id)

    def delete(self, entity_id: int) -> Optional[E]:
        with Session(engine) as session:
            entity = self.get_entity_by_id(entity_id)
            if entity:
                session.execute(students.delete().where(students.c.id == entity_id))
                session.commit()
            return entity
