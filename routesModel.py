from typing import Union

from fastapi import APIRouter

from src.infra.controller.todoController import router as todo_router

router = APIRouter()

@router.get("/")
def read_root():
    return {"Hello": "World"}


router.include_router(todo_router)
