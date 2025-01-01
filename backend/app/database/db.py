import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Load environment variables
load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")

# Create engine and session
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

# Declarative base for models
Base = declarative_base()

# Function to initialize the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
