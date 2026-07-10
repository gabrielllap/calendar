from sqlalchemy import Column, Integer, String, ForeignKey
from database import Base


class Event(Base):
    __tablename__ = "events"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    location = Column(String)
    date = Column(String)
    user_id = Column(Integer, ForeignKey("users.id"))