import time
import logging
from app.database import get_db
from app.models import User
from redis import Redis
import os

redis = Redis(host=os.getenv("REDIS_HOST", "localhost"), port=6379)

def check_database_status():
    try:
        db = next(get_db())
        if db.query(User).count() > 0:
            return True
        return False
    except Exception as e:
        logging.error(f"Ошибка подключения к базе данных: {e}")
        return False

def check_redis_status():
    try:
        redis.set('ping', 'pong')
        return redis.get('ping') == b'pong'
    except Exception as e:
        logging.error(f"Ошибка подключения к Redis: {e}")
        return False

async def get_trade_data_with_cache(pair: str):
    cache_key = f"trade_data_{pair}"
    cached_data = redis.get(cache_key)
    if cached_data:
        logging.info(f"Данные для {pair} получены из кэша.")
        return cached_data.decode('utf-8')
    from app.services.blockchain_integration import get_trade_data
    data = await get_trade_data(pair)
    redis.setex(cache_key, 600, data)  # Кэшируем на 10 минут
    logging.info(f"Данные для {pair} сохранены в кэш.")
    return data