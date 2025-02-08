from celery import Celery
from app.services.blockchain_integration import get_trade_data, get_historical_data

celery_app = Celery('tasks', broker='redis://localhost:6379/0')

@celery_app.task
def fetch_large_data(pair: str):
    data = get_trade_data(pair)
    historical_data = get_historical_data(pair, 30)
    # Сохранение данных в базу данных или дальнейшая обработка
    return data, historical_data
