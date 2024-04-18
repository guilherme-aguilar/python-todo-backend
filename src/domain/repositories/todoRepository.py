from abc import ABC, abstractmethod
from typing import List

from src.domain.models.todoEntity import TodoEntity

class TodoRepository(ABC):
    
    @abstractmethod
    def create(self, todo: TodoEntity) -> None:
        pass

    @abstractmethod
    def findById(self, id: str) -> TodoEntity or None:
        pass

    @abstractmethod
    def find_all(self) -> List[TodoEntity]:
        pass

    @abstractmethod
    def update(self, todo: TodoEntity) -> None:
        pass