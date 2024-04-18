from sqlalchemy.orm import Session
from typing import List
from src.domain.models.todoEntity import TodoEntity
from src.domain.repositories.todoRepository import TodoRepository
from src.infra.databaseSchema.todoSchema import TodoDatabaseSchema
from src.infra.configuration.sqlAlchemyConfiguration import get_db_session  # Importe a função que retorna o gerenciador de contexto

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
        
            # Adicionar o schema_todo ao contexto da sessão
            db_session.add(schema_todo)
        
            # Commit para persistir no banco de dados
            db_session.commit()

    def findById(self, id: int):
        # Implementação para encontrar um todo pelo ID
        pass

    def find_all(self):
        # Implementação para encontrar todos os todos
        pass

    def update(self, todo):
        # Implementação para atualizar um todo
        pass