from celery import Celery
import requests

celery_app = Celery('tasks', broker='redis://localhost:6379/0')

@celery_app.task
def fetch_data_from_api():
    response = requests.get('https://api.dex.com/transactions')
    data = response.json()
    # Сохранить в БД или обработать
