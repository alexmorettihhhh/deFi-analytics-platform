import requests
from typing import List

def send_trade_signal(signal: str, chat_id: str, token: str):
    """Отправка торгового сигнала через Telegram"""
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    data = {
        "chat_id": chat_id,
        "text": signal
    }
    response = requests.post(url, data=data)
    return response.json()

def generate_trade_signal(price_change: float, threshold: float) -> str:
    """Генерация торгового сигнала на основе изменения цены"""
    if abs(price_change) >= threshold:
        return f"Внимание! Цена изменилась на {price_change}%. Возможная торговая возможность!"
    return "Изменение цены незначительное."
