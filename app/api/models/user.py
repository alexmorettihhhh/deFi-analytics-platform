from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.database import Base, get_db

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    password = Column(String)

def get_db():
    db = next(get_db())
    try:
        yield db
    finally:
        db.close()
