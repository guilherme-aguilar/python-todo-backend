from src.domain.models.todoEntity import TodoEntity


class TodoMapper:
    @staticmethod
    def DomainToHttp(raw: TodoEntity) -> dict:
        return {
            "id": raw.id,
            "title": raw.title,
            "description": raw.description,
            "status": raw.status,
            "created_at":raw.created_at,
            "updated_at": raw.updated_at,
        }
        
    @staticmethod
    def DomainToDatabase(raw: TodoEntity) -> dict:
        return {
            "id": raw.id,
            "title": raw.title,
            "description": raw.description,
            "status": raw.status,
            "created_at":raw.created_at,
            "updated_at": raw.updated_at,
        }
        
    @staticmethod
    def DatabaseToDomain(raw: TodoEntity) -> TodoEntity:
        return TodoEntity({
            "title": raw.title,
            "description": raw.description,
            "status": raw.status,
            "created_at":raw.created_at,
            "updated_at": raw.updated_at,
        }, raw.id)
        