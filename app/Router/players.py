from fastapi import APIRouter, status, Depends
from sqlmodel import Session
from ..database.models import PlayerDb,PlayerIn, PlayerSingle, EventIn
from ..database import players_crud as crud
from ..database.database import get_session

router = APIRouter(prefix="/players", tags=["Players"])

@router.get("", response_model=list[PlayerDb])
def get_all_players(*, session: Session = Depends(get_session), player_name: str):
        return crud.get_all_players(session, player_name)
    
@router.post("",status_code=status.HTTP_201_CREATED, response_model=PlayerSingle)
def create_new_player(*, session:Session = Depends(get_session), player_in:PlayerIn):
    return crud.create_new_player(session, player_in)

@router.get("/{id}", response_model=PlayerSingle)
def get_players_by_id(*, session:Session = Depends(get_session), player_id:int):
    return crud.get_players_by_id(session, player_id)

@router.get("/{id}/events", response_model=list[PlayerDb])
def get_players_events_by_player_id(*, session:Session = Depends(get_session), player_name:str):
    return crud.get_all_events_by_player_id(session, player_name)

@router.post("/{id}/events", status_code=status.HTTP_201_CREATED, response_model=PlayerSingle)
def create_new_event_for_player(*, session: Session = Depends(get_session), event_in:EventIn):
    return crud.create_new_event_for_player(session, event_in)