from fastapi import APIRouter, Depends


router = APIRouter()

@router.get("/todo", response_model=None)
async def create_todo():
  return "todo!"