from fastapi import Response,HTTPException, status
from .models import PlayerIn,PlayerDb, EventIn, EventDb
from sqlmodel import Session, select,case

# Allowed types for event class type:str
ALLOWED_TYPES= ["level_started", "level_solved"]

#function that gets all players from database and returns them to router.
def get_all_players(session: Session):
    return session.exec(select(PlayerDb)).all() #query for all players from database.

#creates new player to database and returns created player with id to database.
def create_new_player(session:Session, player_in: PlayerIn):
    player = PlayerDb.model_validate(player_in) #validates type and creates object.
    session.add(player) # adds player to database
    session.commit() #commits player to database
    session.refresh(player) 
    return player

#gets players information by id from database and returns it to crud.
def get_players_by_id(session:Session, player_id: int):
    player = session.get(PlayerDb, player_id)
    if not player: #if player not found raises exception.
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return player

#gets all events by player id from database. Can also get all type events from database. and returns results to router.
def get_events_by_player_id(session:Session, player_id: int, event_type: str = None):
    if event_type is not None and event_type not in ALLOWED_TYPES: #checks that input isn't either None or allowed type. if both true raises exception.
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
    player_exists = session.exec(select(PlayerDb.id).where(PlayerDb.id==player_id)).first() #query player by id.
    if player_exists == None: #checks if query returns None and raises exception if true.
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    events = session.exec(select(EventDb).where(EventDb.player_id==player_id)).all() #query for every event that include player id.
    if event_type:
        events = session.exec(select(EventDb).where(EventDb.player_id==player_id,EventDb.type==event_type)).all() # query if event type has been given and returns all events that include player id and event type.
    return events

#creates new event for certain player and returns it to router.
def create_new_event_for_player(session:Session,player_id:int, event_in:EventIn):
    event = EventDb(type=event_in.type,detail=event_in.detail, player_id=player_id)
    if event.type not in ALLOWED_TYPES:  #checks that input isn't allowed type and if not raises exception.
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
    player_exists = session.exec(select(PlayerDb.id).where(PlayerDb.id==player_id)).first() 
    if player_exists == None: #checks that player id exists and if not raises exception.
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    session.add(event) #adds player to database
    session.commit() #commits player to database
    session.refresh(event)
    return event