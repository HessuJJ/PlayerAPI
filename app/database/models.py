from sqlmodel import SQLModel, Field, Relationship

class PlayerBase(SQLModel):
    name:str

class PlayerIn(PlayerBase):
    pass
    
class PlayerDb(PlayerBase, table = True):
    id:int = Field(default=None, primary_key = True)
    events: list["EventDb"] = Relationship(back_populates="events")
    
class PlayerSingle(SQLModel):
    id:int
    name:str

class EventBase(SQLModel):
    type:str
    detail:str
class EventIn(EventBase):
    pass

class EventDb(EventBase, table = True):
    id:int = Field(default=None, primary_key= True)
    timestamp:str
    player_id: int | None = Field(default=None, foreign_key="playerdb.id")
    