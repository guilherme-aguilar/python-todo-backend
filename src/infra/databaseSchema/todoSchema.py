from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import validates

Base = declarative_base()

class TodoDatabaseSchema(Base):
    __tablename__ = 'todos'

    id = Column(String, primary_key=True)
    title = Column(String)
    description = Column(String)
    status = Column(String)
    created_at = Column(DateTime,)
    updated_at = Column(DateTime, nullable=True)

 