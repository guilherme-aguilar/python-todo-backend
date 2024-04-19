from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.infra.configuration.sqlAlchemyConfiguration import get_db_session

from src.infra.repositories.todoDatabaseRepository import SqlAlchemyTodoRepository

from src.infra.mappers.todoMapper import TodoMapper

router = APIRouter()


@router.get("/todo", response_model=None)
async def todo():
    return "todo!"

from src.useCases.todo.newTodoUseCase import NewTodoUseCase, Request as RequestNew

@router.post("/todo/new", response_model=None)
async def newTodo(request: RequestNew, db: Session = Depends(get_db_session)):
    
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

from src.useCases.todo.editStatusTodoUseCase import EditStatusTodoUseCase, Request as RequestUpdateStatus

@router.put("/todo/updateStatus", response_model=None)
async def listAllTodo(request: RequestUpdateStatus , db: Session = Depends(get_db_session)):
    
    todoEntity =  await EditStatusTodoUseCase(SqlAlchemyTodoRepository(db)).execute(request)
    
    return TodoMapper.DomainToHttp(todoEntity.data)

from src.useCases.todo.editTodoUseCase import EditTodoUseCase

from src.infra.controller.todoDto import UpdateTodoDto

@router.put("/todo/update", response_model=None)
async def listAllTodo(request: UpdateTodoDto , db: Session = Depends(get_db_session)):
    
    todoEntity =  await EditTodoUseCase(SqlAlchemyTodoRepository(db)).execute(request)
    
    return TodoMapper.DomainToHttp(todoEntity.data)