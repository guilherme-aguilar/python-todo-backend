from src.domain.repositories.todoRepository import TodoRepository
from src.domain.models.todoEntity import TodoEntity
from pydantic import BaseModel

class Request(BaseModel):
    title: str
    description: str

class Response(BaseModel):
    data: TodoEntity

class NewTodoUseCase:
    def __init__(self, TodoRepository: TodoRepository):
        self.TodoRepository = TodoRepository
        
    async def execute(self, request: Request) -> Response:
        
        todo = TodoEntity(
            title=request.title, 
            description=request.description
        )

        await self.TodoRepository.create(todo)
        
        return Response(
          data = todo
          )
