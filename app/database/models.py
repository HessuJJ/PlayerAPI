from sqlmodel import SQLModel, Field, Relationship
from datetime import datetime


class PlayerBase(SQLModel):
    name:str

class PlayerIn(PlayerBase):
    pass

#class that has relationship to EventDb player
class PlayerDb(PlayerBase, table = True):
    id:int = Field(default=None, primary_key = True)
    events: list["EventDb"] = Relationship(back_populates="player")
    
class PlayerSingle(SQLModel):
    id:int
    name:str

class EventBase(SQLModel):
    type:str
    detail:str
class EventIn(EventBase):
    pass

#class that has relationship to PlayerDb events
class EventDb(EventBase, table = True):
    id:int = Field(default=None, primary_key= True)
    timestamp: datetime = Field(default_factory=datetime.utcnow)
    player_id: int = Field(default=None, foreign_key="playerdb.id")
    player: PlayerDb = Relationship(back_populates="events")
    