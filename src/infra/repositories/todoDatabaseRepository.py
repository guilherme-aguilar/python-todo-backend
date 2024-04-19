from sqlalchemy.orm import Session
from typing import List
from src.domain.models.todoEntity import TodoEntity
from src.domain.repositories.todoRepository import TodoRepository
from src.infra.databaseSchema.todoSchema import TodoDatabaseSchema
from src.infra.configuration.sqlAlchemyConfiguration import get_db_session
from src.infra.mappers.todoMapper import TodoMapper

class SqlAlchemyTodoRepository(TodoRepository):
    def __init__(self, db_session: Session):
        self.db_session = db_session
        
    async def create(self, TodoEntity: TodoEntity) -> None:
        with get_db_session() as db_session:
            todoDatabase = TodoMapper.DomainToDatabase(TodoEntity)
            schema_todo = TodoDatabaseSchema(**todoDatabase)
            db_session.add(schema_todo)
            db_session.commit()

    async def findById(self, id: int) -> TodoEntity or None:
        with get_db_session() as db_session:
            data = db_session.query(TodoDatabaseSchema).filter_by(id=id).first()
            return TodoMapper.DatabaseToDomain(data)

    async def find_all(self) -> List[TodoEntity] or []:
        with get_db_session() as db_session:
            listDatabase = db_session.query(TodoDatabaseSchema).all()
            return list(map(TodoMapper.DatabaseToDomain, listDatabase))
        
    async def update(self, TodoEntity: TodoEntity):
        with get_db_session() as db_session:
            todoDatabase = TodoMapper.DomainToDatabase(TodoEntity)
            schema_todo = TodoDatabaseSchema(**todoDatabase)
            existing_todo = db_session.query(TodoDatabaseSchema).filter_by(id=schema_todo.id).first()
          
            if existing_todo:
                for key, value in todoDatabase.items():
                    if value is not None:  # Verifica se o valor não é None
                        setattr(existing_todo, key, value)
                db_session.commit()
                
    async def delete(self, id: str):
        with get_db_session() as db_session:

            db_session.query(TodoDatabaseSchema).filter_by(id=id).delete()
            db_session.commit()
