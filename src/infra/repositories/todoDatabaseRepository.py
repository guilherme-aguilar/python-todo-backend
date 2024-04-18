from sqlalchemy.orm import Session
from typing import List
from src.domain.models.todoEntity import TodoEntity
from src.domain.repositories.todoRepository import TodoRepository
from src.infra.databaseSchema.todoSchema import TodoDatabaseSchema
from src.infra.configuration.sqlAlchemyConfiguration import get_db_session  # Importe a função que retorna o gerenciador de contexto

from src.infra.mappers.todoMapper import TodoMapper
class SqlAlchemyTodoRepository(TodoRepository):
    def __init__(self, db_session: Session):
        self.db_session = db_session
        
    async def create(self, TodoEntity: TodoEntity) -> None:
        with get_db_session() as db_session:
  
            schema_todo = TodoDatabaseSchema(
                id=TodoEntity.id,
                title=TodoEntity.title,
                description=TodoEntity.description,
                status=TodoEntity.status,
                created_at=TodoEntity.created_at,
                updated_at=TodoEntity.updated_at
                )
        
            db_session.add(schema_todo)
        
            db_session.commit()

    def findById(self, id: int):
        pass

    async def find_all(self) -> List[TodoEntity]:
        with get_db_session() as db_session:
            listDatabase = db_session.query(TodoDatabaseSchema).all()
            return list(map(TodoMapper.DatabaseToDomain, listDatabase))
        

    def update(self, todo):
        # Implementação para atualizar um todo
        pass