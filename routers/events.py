from fastapi import APIRouter
from schemas.event import Event

router = APIRouter()

@router.post("/events")
def create_event(event: Event):
    return {
        "message": "Eveniment creat!",
        "event": event
    }