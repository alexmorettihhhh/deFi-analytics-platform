import requests

def send_telegram_notification(message: str, chat_id: str, token: str):
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    data = {"chat_id": chat_id, "text": message}
    response = requests.post(url, data=data)
    return response.json()

# Пример использования
send_telegram_notification("New trading signal: Buy ETH", "<chat_id>", "<bot_token>")
