from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class UpdateTodoRequest(BaseModel):
    id: str
    title : Optional[str] = None
    description : Optional[str] = None
    
class UpdateTodoResponse(BaseModel):
    id: str
    title: str
    description: str
    status: str
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    
