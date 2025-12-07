from fastapi import Response,HTTPException, status
from .models import EventIn, EventDb
from sqlmodel import Session, select


ALLOWED_TYPES= ["level_started", "level_solved"]

def get_all_events(session:Session, event_type:str = None):
    event = session.exec(select(EventDb)).all() 
    if event_type:
        if event_type not in ALLOWED_TYPES:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
        event = session.exec(select(EventDb).where(EventDb.type == event_type)).all()
    return event

