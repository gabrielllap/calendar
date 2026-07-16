from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import get_db
from models.event import Event
from models.user import User
from schemas.event import EventCreate
from security import get_current_user

router = APIRouter()

@router.post("/events")
def create_event(
    event: EventCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    new_event = Event(
        title=event.title,
        description=event.description,
        date=event.date,
        time=event.time,
        location=event.location,
        user_id=current_user.id
    )

    db.add(new_event)
    db.commit()
    db.refresh(new_event)

    return {
        "message": "Event created successfully",
        "event": {
            "id": new_event.id,
            "title": new_event.title,
            "description": new_event.description,
            "date": new_event.date,
            "time": new_event.time,
            "location": new_event.location,
            "user_id": new_event.user_id
        }
    }

@router.get("/events")
def get_events(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    events = db.query(Event).filter(
        Event.user_id == current_user.id
    ).all()

    return events

@router.get("/events/{event_id}")
def get_event(
    event_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    event = db.query(Event).filter(
        Event.id == event_id,
        Event.user_id == current_user.id
    ).first()

    if event is None:
        raise HTTPException(
            status_code=404,
            detail="Event not found"
        )

    return event