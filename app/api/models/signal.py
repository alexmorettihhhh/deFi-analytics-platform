import requests
import logging

def send_trade_signal(signal: str, chat_id: str, token: str):
    """Отправка торгового сигнала через Telegram"""
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    data = {
        "chat_id": chat_id,
        "text": signal
    }
    try:
        response = requests.post(url, data=data)
        if response.status_code != 200:
            logging.error(f"Ошибка при отправке сигнала: {response.status_code} - {response.text}")
            return {"error": "Failed to send signal"}
        return response.json()
    except requests.exceptions.RequestException as e:
        logging.error(f"Ошибка при отправке сигнала: {e}")
        return {"error": "Failed to send signal"}

def generate_trade_signal(price_change: float, threshold: float) -> str:
    """Генерация торгового сигнала на основе изменения цены"""
    if abs(price_change) >= threshold:
        return f"Внимание! Цена изменилась на {price_change}%. Возможная торговая возможность!"
    return "Изменение цены незначительное."
