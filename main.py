from fastapi import FastAPI

from routers.users import router as users_router
from routers.events import router as events_router

app = FastAPI(title="Practica FastAPI")

app.include_router(users_router)
app.include_router(events_router)