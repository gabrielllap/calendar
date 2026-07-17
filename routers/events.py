from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import get_db
from models.event import Event
from models.user import User
from schemas.event import (
    EventCreate,
    EventUpdate,
    EventResponse,
    EventMessageResponse
)
from security import get_current_user

router = APIRouter()

def get_user_event(
    event_id: int,
    current_user: User,
    db: Session
):
    event = db.query(Event).filter(
        Event.id == event_id
    ).first()

    if event is None:
        raise HTTPException(
            status_code=404,
            detail="Event not found"
        )

    if event.user_id != current_user.id:
        raise HTTPException(
            status_code=403,
            detail="You are not allowed to access this event"
        )

    return event

@router.post(
    "/events",
    response_model=EventMessageResponse
)
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
        "event": new_event
    }

@router.get(
    "/events",
    response_model=list[EventResponse]
)
def get_events(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    events = db.query(Event).filter(
        Event.user_id == current_user.id
    ).all()

    return events

@router.get(
    "/events/{event_id}",
    response_model=EventResponse
)
def get_event(
    event_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    event = get_user_event(
        event_id,
        current_user,
        db
    )

    return event

@router.put("/events/{event_id}")
def update_event(
    event_id: int,
    event_data: EventUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    event = get_user_event(
        event_id,
        current_user,
        db
    )

    event.title = event_data.title
    event.description = event_data.description
    event.date = event_data.date
    event.time = event_data.time
    event.location = event_data.location

    db.commit()
    db.refresh(event)

    return {
        "message": "Event updated successfully",
        "event": event
    }
@router.delete("/events/{event_id}")
def delete_event(
    event_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    event = get_user_event(
        event_id,
        current_user,
        db
    )

    db.delete(event)
    db.commit()

    return {
        "message": "Event deleted successfully"
    }