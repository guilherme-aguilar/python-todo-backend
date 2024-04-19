from src.domain.repositories.todoRepository import TodoRepository
from src.domain.models.todoEntity import TodoEntity
from pydantic import BaseModel


class Response(BaseModel):
    data: list[TodoEntity]

class ListAllTodoUseCase:
    def __init__(self, TodoRepository: TodoRepository):
        self.TodoRepository = TodoRepository
        
    async def execute(self) -> Response:
        
        todoList = await self.TodoRepository.find_all()
        
        return Response(
          data = todoList
          )
