from dataclasses import dataclass, field
from typing import Optional
from uuid import uuid4
from datetime import datetime

@dataclass
class TodoM:
    title: str
    description: str
    status: str
    created_at: datetime
    updated_at: Optional[datetime] = None

@dataclass 
class TodoEntity:
    def __init__(
        self,
        title: str,
        description: str,
        status: Optional[str] = "pendente",
        created_at: datetime = datetime.now(),
        updated_at: Optional[datetime] = None,
        id: Optional[str] = None
    ):
        self._id = id or str(uuid4())
        self.props = TodoM(title, description, status,created_at, updated_at)

    @property
    def id(self) -> str:
        return self._id

    @property
    def title(self) -> str:
        return self.props.title

    @title.setter
    def title(self, value: str):
        if (self.props.title != None) : self.updated()
        self.props.title = value

    @property
    def description(self) -> str:
        return self.props.description

    @description.setter
    def description(self, value: str):
        if (self.props.description != None) : self.updated()
        self.props.description = value

    @property
    def status(self) -> Optional[str]:
      return self.props.status

    @property
    def created_at(self) -> datetime:
        return self.props.created_at
    
    @property
    def updated_at(self) -> datetime:
        return self.props.updated_at

    @property
    def updated(self) -> None:
        self.props.updated_at = datetime.now()

    def setStatusInProgress(self):
        self.props.status = "em andamento"
        self.updated()

    def setStatusCompleted(self):
        self.props.status = "concluído"
        self.updated()
        

    def to_model(self) -> TodoM:
        return self.props
