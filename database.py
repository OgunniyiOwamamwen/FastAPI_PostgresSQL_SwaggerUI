from sqlalchemy import create_engine
from sqlalchemy.orm  import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base  = declarative_base()

URL_DATABLE = 'postgresql://postgres:419m1@localhost:5433/quizapplication'

engine = create_engine(URL_DATABLE)

SessionLocal = sessionmaker(autocommit =False, autoflush=False, bind=engine)