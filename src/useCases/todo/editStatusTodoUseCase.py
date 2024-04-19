
from enum import Enum
from src.domain.repositories.todoRepository import TodoRepository
from src.domain.models.todoEntity import TodoEntity
from pydantic import BaseModel

class StatusEnum(str, Enum):
    em_andamento = "em andamento"
    concluido = "finalizado"

class Request(BaseModel):
    id: str
    status: StatusEnum

class Response(BaseModel):
    data: TodoEntity

class EditStatusTodoUseCase:
    def __init__(self, TodoRepository: TodoRepository):
        self.TodoRepository = TodoRepository
        
    async def execute(self, request: Request) -> Response:
        
        oldData : TodoEntity = await self.TodoRepository.findById(request.id)
        
        if oldData is not None:
            if request.status == "em andamento":
                oldData.setStatusInProgress()


            if request.status == "finalizado":
                oldData.setStatusCompleted()


            
        await self.TodoRepository.update(oldData)
        
        return Response(
          data = oldData
          )
