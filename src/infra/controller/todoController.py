from fastapi import APIRouter

from src.domain.models.todoEntity import TodoEntity 
from src.infra.mappers.todoMapper import TodoMapper

router = APIRouter()


@router.get("/todo", response_model=None)
async def todo():
    return "todo!"

@router.post("/todo/new", response_model=None)
async def newTodo():
    return "new Todo!"
  
@router.get("/todo/list", response_model=None)
async def newTodo():
    return "Todos!"