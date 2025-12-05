from sqlmodel import Session, create_engine, SQLModel

connect_args  = {"check_same_thread": False}
engine = create_engine("sqlite:///scoreboard.db", echo=True, connect_args=connect_args)

def create_db():
    SQLModel.metadata.create_all(engine)
    
def get_session():
    session = Session(engine)
    try:
        yield session
    finally:
        session.close()