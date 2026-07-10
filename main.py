from fastapi import FastAPI
from database import Base, engine

# Import SQLAlchemy models
from models.user import User
from models.event import Event

# Import routers
from routers.users import router as users_router
from routers.events import router as events_router

# Create tables in data base
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Practica FastAPI")

app.include_router(users_router)
app.include_router(events_router)