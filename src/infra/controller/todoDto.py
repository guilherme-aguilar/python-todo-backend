from typing import Optional
from pydantic import BaseModel


class UpdateTodoDto(BaseModel):
    id: str
    title : Optional[str] = None
    description : Optional[str] = None

