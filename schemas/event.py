from pydantic import BaseModel

class Event(BaseModel):
    title: str
    location: str
    date: str