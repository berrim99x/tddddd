from fastapi import FastAPI
from src.interface.controllers.user_controller import router as user_router

app = FastAPI()
app.include_router(user_router)
