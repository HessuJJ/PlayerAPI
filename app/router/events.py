from fastapi import APIRouter, Depends
from sqlmodel import Session
from ..database.models import EventDb
from ..database import events_crud as crud
from ..database.database import get_session

# Router that defines to endpoints URL-root "/events" and groups them to tag "events"
router = APIRouter(prefix="/events", tags=["events"])

#Router get that calls crud function that gets all events.
@router.get("", response_model=list[EventDb])
def get_all_events(*, session:Session = Depends(get_session), event_type:str = None):
    return crud.get_all_events(session, event_type)