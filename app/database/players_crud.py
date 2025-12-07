from fastapi import Response,HTTPException, status
from .models import PlayerIn,PlayerDb, EventIn, EventDb
from sqlmodel import Session, select,case

ALLOWED_TYPES= ["level_started", "level_solved"]

def get_all_players(session: Session):
    return session.exec(select(PlayerDb)).all()

def create_new_player(session:Session, player_in: PlayerIn):
    player = PlayerDb.model_validate(player_in)
    session.add(player)
    session.commit()
    session.refresh(player)
    return player

def get_players_by_id(session:Session, player_id: int):
    player = session.get(PlayerDb, player_id)
    if not player:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return player

def get_events_by_player_id(session:Session, player_id: int, event_type: str = None):
    if event_type is not None and event_type not in ALLOWED_TYPES:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
    player_exists = session.exec(select(PlayerDb.id).where(PlayerDb.id==player_id)).first()
    if player_exists == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    print(player_exists)
    events = session.exec(select(EventDb).where(EventDb.player_id==player_id)).all()
    if event_type:
        events = session.exec(select(EventDb).where(EventDb.player_id==player_id,EventDb.type==event_type)).all()
    return events

def create_new_event_for_player(session:Session,player_id:int, event_in:EventIn):
    event = EventDb(type=event_in.type,detail=event_in.detail, player_id=player_id)
    if event.type not in ALLOWED_TYPES:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
    if not event.player_id:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    session.add(event)
    session.commit()
    session.refresh(event)
    return event