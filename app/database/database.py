from sqlmodel import Session, create_engine, SQLModel

#allows database to use from multiple threads
connect_args  = {"check_same_thread": False}

#Creates database engine for sqlite-file "scoreboard.db". echo prints all sql-commands to console
engine = create_engine("sqlite:///scoreboard.db", echo=True, connect_args=connect_args)

#creates database tables if not created
def create_db():
    SQLModel.metadata.create_all(engine)

# FastAPI-dependecy that returns database session
def get_session():
    session = Session(engine) # creates sql-session object
    try:
        yield session #yields session to router and crud
    finally:
        session.close() #closes database connection