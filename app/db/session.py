from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from app.config import settings

DATABASE_URL = settings.DATABASE_URL

engine = create_engine(
    DATABASE_URL,
    echo=False,
    pool_pre_ping=True
)

SessionLocal = scoped_session(
    sessionmaker(
        autocommit=False,
        autoflush=False,
        bind=engine
     )
)

def get_db():
    """ 
        Provides a database session to the application. 
        Ensures the session is closed after use. 
    """


    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()