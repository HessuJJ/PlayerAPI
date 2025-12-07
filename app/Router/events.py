from fastapi import APIRouter, status, Depends
from sqlmodel import Session
from ..database.models import EventDb
from ..database import events_crud as crud
from ..database.database import get_session

router = APIRouter(prefix="/events", tags=["events"])

@router.get("", response_model=list[EventDb])
def get_all_events(*, session:Session = Depends(get_session), event_type:str = None):
    return crud.get_all_events(session, event_type)