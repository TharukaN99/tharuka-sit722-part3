from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

SQLALCHEMY_DATABASE_URL = "postgresql://tharuka_sit722_part3_user:kujg7KYIxL90r3TzLHO9P6reOIMu1mDf@dpg-crmqmb08fa8c73anclq0-a.oregon-postgres.render.com/tharuka_sit722_part3" #os.getenv("DATABASE_URL")

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
