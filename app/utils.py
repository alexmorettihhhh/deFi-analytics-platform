import time
import logging
from app.database import get_db
from app.models import User
from redis import Redis
import os

# Инициализация Redis
redis = Redis(host=os.getenv("REDIS_HOST", "localhost"), port=6379)

def check_database_status():
    """Проверка доступности базы данных"""
    try:
        # Проверяем наличие соединения с БД
        db = get_db()
        if db.query(User).count() > 0:
            return True
        return False
    except Exception as e:
        logging.error(f"Ошибка подключения к базе данных: {e}")
        return False

def check_redis_status():
    """Проверка состояния Redis"""
    try:
        # Пробуем получить и установить ключ в Redis
        redis.set('ping', 'pong')
        return redis.get('ping') == b'pong'
    except Exception as e:
        logging.error(f"Ошибка подключения к Redis: {e}")
        return False

async def get_trade_data_with_cache(pair: str):
    """Получение торговых данных с кэшированием"""
    cache_key = f"trade_data_{pair}"
    cached_data = redis.get(cache_key)
    
    if cached_data:
        logging.info(f"Данные для {pair} получены из кэша.")
        return cached_data.decode('utf-8')
    
    # Здесь будет логика для получения данных, например, с API или базы данных
    data = await get_trade_data(pair)
    
    # Сохраняем в кэш на 10 минут
    redis.setex(cache_key, 600, data)
    logging.info(f"Данные для {pair} сохранены в кэш.")
    return data
