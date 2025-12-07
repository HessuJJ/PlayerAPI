from contextlib import asynccontextmanager
from fastapi import FastAPI
from .router import players, events
from .database.database import create_db 

#lifespan function is run when the application starts
@asynccontextmanager
async def lifespan(app:FastAPI):
    create_db() #creates database if not already created
    yield #returns results and continues to next step

#creates fastapi-app and gives it function lifespan
app = FastAPI(lifespan=lifespan)

#register routes to app
app.include_router(players.router)
app.include_router(events.router)
