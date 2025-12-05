from fastapi import Response,HTTPException, status
from .models import PlayerIn,PlayerDb
from sqlmodel import Session, select


def get_all_players(session: Session, player: int = -1):
    return session.exec(select(PlayerDb)).all

def create_new_player(session:Session, player_in: PlayerIn):
    player = PlayerDb.model_validate(player_in)
    session.add(player)
    session.commit()
    session.refresh(player)
    return player

def get_players_by_id(session:Session, player_id: int):
    player = session.get(PlayerDb, player_id)
    if not player:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Player with id {player_id} not found.")
    return player
