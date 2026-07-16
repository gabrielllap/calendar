from fastapi import FastAPI

from database import Base, engine
from models.event import Event
from models.user import User
from routers.events import router as events_router
from routers.users import router as users_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Practica FastAPI")

app.include_router(users_router)
app.include_router(events_router)