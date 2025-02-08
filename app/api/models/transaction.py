import asyncpg
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Transaction(Base):
    __tablename__ = 'transactions'
    id = Column(Integer, primary_key=True, index=True)
    token_name = Column(String)
    price = Column(Integer)
    volume = Column(Integer)

async def get_transactions():
    # Подключение к базе данных
    conn = await asyncpg.connect(user='user', password='password', database='defidb')
    result = await conn.fetch('SELECT * FROM transactions LIMIT 10')
    return result
