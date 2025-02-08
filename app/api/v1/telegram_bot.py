import logging
import requests
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from telegram.ext import MessageHandler, Filters
import os

# Настройка логирования
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Функция для отправки сообщения в Telegram
def send_telegram_message(chat_id, message):
    token = 'YOUR_BOT_API_TOKEN'  # Замените на ваш токен
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    data = {
        'chat_id': chat_id,
        'text': message
    }
    response = requests.post(url, data=data)
    return response.json()

# Обработчик команды /start
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Привет! Я твой бот для получения торговых сигналов.\nВведите /signal для получения торговых сигналов.")

# Обработчик команды /signal
def signal(update: Update, context: CallbackContext) -> None:
    chat_id = update.message.chat_id
    signal_text = "Торговый сигнал: покупка BTC!"  # Пример торгового сигнала
    send_telegram_message(chat_id, signal_text)
    update.message.reply_text("Торговый сигнал отправлен!")

# Обработчик для получения сообщений от пользователя
def handle_message(update: Update, context: CallbackContext) -> None:
    user_message = update.message.text
    chat_id = update.message.chat_id
    send_telegram_message(chat_id, f"Вы сказали: {user_message}")

# Функция для запуска бота
def main():
    # Ваш Telegram токен, полученный от BotFather
    token = 'YOUR_BOT_API_TOKEN'  # Замените на ваш токен

    updater = Updater(token, use_context=True)

    # Получаем диспетчера для регистрации обработчиков
    dispatcher = updater.dispatcher

    # Регистрируем обработчики команд
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("signal", signal))

    # Обработчик для обычных сообщений
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    # Запуск бота
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
