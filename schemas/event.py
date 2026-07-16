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