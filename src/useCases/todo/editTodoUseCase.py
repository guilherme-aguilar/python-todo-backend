
from enum import Enum
from src.domain.repositories.todoRepository import TodoRepository
from src.domain.models.todoEntity import TodoEntity
from pydantic import BaseModel

from typing import Optional



class Request(BaseModel):
    id: str

class Response(BaseModel):
    data: TodoEntity

class EditTodoUseCase:
    def __init__(self, TodoRepository: TodoRepository):
        self.TodoRepository = TodoRepository
        
    async def execute(self, request: Request) -> Response:
        
        oldData : TodoEntity = await self.TodoRepository.findById(request.id)
        
         # Construir o dicionário 'others' apenas com os campos opcionais presentes em request
        others = {}
        if request.title is not None:
            others['title'] = request.title
        if request.description is not None:
            others['description'] = request.description
        
        # Comparar oldData e others, caso tenha alterações de valores, os valores novos devem ser alocados
        for key, value in others.items():
            if getattr(oldData, key) != value:
                setattr(oldData, key, value)
        
        await self.TodoRepository.update(oldData)
        
        return Response(
          data = oldData
          )
