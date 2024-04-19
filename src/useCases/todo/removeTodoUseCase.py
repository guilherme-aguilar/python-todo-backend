
from enum import Enum
from src.domain.repositories.todoRepository import TodoRepository
from src.domain.models.todoEntity import TodoEntity
from pydantic import BaseModel


class RemoveTodoUseCase:
    def __init__(self, TodoRepository: TodoRepository):
        self.TodoRepository = TodoRepository
        
    async def execute(self, id: str) -> None:
        
        await self.TodoRepository.delete(id)
        
       