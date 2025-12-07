from fastapi import APIRouter, status, Depends
from sqlmodel import Session
from ..database.models import PlayerDb,PlayerIn, PlayerSingle, EventIn, EventDb
from ..database import players_crud as crud
from ..database.database import get_session

router = APIRouter(prefix="/players", tags=["Players"])

@router.get("", response_model=list[PlayerDb])
def get_all_players(*, session: Session = Depends(get_session)):
        return crud.get_all_players(session)
    
@router.post("",status_code=status.HTTP_201_CREATED, response_model=PlayerSingle)
def create_new_player(*, session:Session = Depends(get_session), player_in:PlayerIn):
    return crud.create_new_player(session, player_in)

@router.get("/{id}", response_model=PlayerDb)
def get_players_by_id(*, session:Session = Depends(get_session), player_id:int):
    return crud.get_players_by_id(session, player_id)


@router.get("/{id}/events", response_model=list[EventDb])
def get_players_events_by_player_id(*,session:Session = Depends(get_session), player_id:int, event_type:str = None):
    return crud.get_events_by_player_id(session,player_id, event_type)

@router.post("/{id}/events", status_code=status.HTTP_201_CREATED, response_model=EventDb)
def create_new_event_for_player(id:int, event_in:EventIn,session: Session = Depends(get_session)):
    return crud.create_new_event_for_player(session, id, event_in)
