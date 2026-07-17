from pydantic import BaseModel


class EventCreate(BaseModel):
    title: str
    description: str
    date: str
    time: str
    location: str

class EventUpdate(BaseModel):
    title: str
    description: str
    date: str
    time: str
    location: str

class EventResponse(BaseModel):
    id: int
    title: str
    description: str
    date: str
    time: str
    location: str
    user_id: int

    class Config:
        from_attributes = True

class EventMessageResponse(BaseModel):
    message: str
    event: EventResponse