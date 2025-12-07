from fastapi import Response,HTTPException, status
from .models import EventIn, EventDb
from sqlmodel import Session, select

# Allowed types for event class type:str
ALLOWED_TYPES= ["level_started", "level_solved"]

#gets all events from database. can also get all certain type events from database. returns events to router.
def get_all_events(session:Session, event_type:str = None):
    event = session.exec(select(EventDb)).all() #gets all events from database.
    if event_type: #checks if event type is given.
        if event_type not in ALLOWED_TYPES: # checks if event type is correct and if not raises exception.
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
        event = session.exec(select(EventDb).where(EventDb.type == event_type)).all() #gets all events form database that are given event type.
    return event

