from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.infra.configuration.sqlAlchemyConfiguration import get_db_session
from src.useCases.todo.newTodoUseCase import NewTodoUseCase, Request


from src.infra.repositories.todoDatabaseRepository import SqlAlchemyTodoRepository

from src.infra.mappers.todoMapper import TodoMapper

router = APIRouter()


@router.get("/todo", response_model=None)
async def todo():
    return "todo!"

@router.post("/todo/new", response_model=None)
async def newTodo(request: Request, db: Session = Depends(get_db_session)):
    
    todoEntity =  await NewTodoUseCase(SqlAlchemyTodoRepository(db)).execute(request)
    
    print(todoEntity.data)
    
    return TodoMapper.DomainToHttp(todoEntity.data)


from src.useCases.todo.ListAllTodoUseCase import ListAllTodoUseCase

@router.get("/todo/list", response_model=None)
async def listAllTodo(db: Session = Depends(get_db_session)):
    
    todoListEntity = await ListAllTodoUseCase(
      SqlAlchemyTodoRepository(db)
      ).execute()
    
    return list(map(TodoMapper.DomainToHttp, todoListEntity.data))