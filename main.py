from fastapi import FastAPI
from routesModel import router

app = FastAPI()

app.include_router(router)