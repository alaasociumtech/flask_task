from typing import Any, Dict, Generic, List, TypeVar

from flask_task.domain.base_entity import BaseEntity

E = TypeVar('E', bound='BaseEntity')


class BaseRepo(Generic[E]):
    def __init__(self) -> None:
        self.entities: Dict[int, E] = {}
        self.counter = 1

    def get_all(self) -> List[E]:
        return (list(self.entities.values()))

    def get_entity_by_id(self, entity_id: int) -> Any:
        return (self.entities.get(entity_id))

    def create(self, entity: E) -> E:
        entity.id = self.counter
        self.entities[self.counter] = entity
        self.counter += 1
        return entity

    def update(self, entity_id: int, updated_entity: E) -> Any:
        if entity_id in self.entities:
            self.entities[entity_id] = updated_entity
            return updated_entity
        return None

    def delete(self, entity_id: int) -> Any:
        return self.entities.pop(entity_id, None)
