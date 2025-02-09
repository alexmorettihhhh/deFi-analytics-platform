import logging
from telegram import Update, Bot, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters, CallbackQueryHandler
from apscheduler.schedulers.background import BackgroundScheduler
import os
import time
from app.signal import generate_trade_signal

logging.basicConfig(level=logging.INFO)

# Установим параметры для бота
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

bot = Bot(token=TELEGRAM_TOKEN)
updater = Updater(token=TELEGRAM_TOKEN, use_context=True)
dispatcher = updater.dispatcher

# Стартовая команда
def start(update: Update, context: CallbackContext):
    """Команда /start - приветствие и инструкции"""
    update.message.reply_text("Привет! Я торговый бот. Используйте /help для получения списка команд.")

# Команда помощи
def help(update: Update, context: CallbackContext):
    """Команда /help - список доступных команд"""
    update.message.reply_text(
        "Доступные команды:\n"
        "/start - Приветствие\n"
        "/help - Список команд\n"
        "/signal - Получить торговый сигнал\n"
        "/status - Проверить текущий статус торгов\n"
        "/buttons - Получить кнопки выбора"
    )

# Получение торгового сигнала
def trade_signal(update: Update, context: CallbackContext):
    """Команда /signal - генерирует торговый сигнал"""
    price_change = 5  # Пример изменения цены
    threshold = 3  # Порог для генерации сигнала
    signal = generate_trade_signal(price_change, threshold)
    update.message.reply_text(signal)

# Получение статуса торгов
def trade_status(update: Update, context: CallbackContext):
    """Команда /status - проверка текущего статуса торгов"""
    # Для примера, просто отправим статус с фиктивными данными
    status_message = "Торговля активна. Прогноз: положительный."
    update.message.reply_text(status_message)

# Кнопки для выбора действия
def button(update: Update, context: CallbackContext):
    """Кнопки для выбора типа сигнала"""
    keyboard = [
        [InlineKeyboardButton("Торговые сигналы", callback_data='trade_signal')],
        [InlineKeyboardButton("Статус торгов", callback_data='trade_status')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text("Выберите действие:", reply_markup=reply_markup)

# Обработка нажатий на кнопки
def button_handler(update: Update, context: CallbackContext):
    """Обработка нажатий на кнопки"""
    query = update.callback_query
    query.answer()
    
    if query.data == 'trade_signal':
        signal = generate_trade_signal(5, 3)  # Пример
        query.edit_message_text(text=f"Получен торговый сигнал:\n{signal}")
    elif query.data == 'trade_status':
        status_message = "Торговля активна. Прогноз: положительный."
        query.edit_message_text(text=status_message)

# Функция для автоматической отправки уведомлений
def send_automatic_notifications():
    """Отправка автоматических уведомлений пользователю о торговых сигналах"""
    price_change = 7  # Например, изменение на 7%
    threshold = 5
    signal = generate_trade_signal(price_change, threshold)
    bot.send_message(chat_id=CHAT_ID, text=signal)

# Настройка периодических задач
scheduler = BackgroundScheduler()
scheduler.add_job(send_automatic_notifications, 'interval', minutes=10)  # Каждые 10 минут
scheduler.start()

# Обработка обычных сообщений
def echo(update: Update, context: CallbackContext):
    """Ответ на обычные текстовые сообщения"""
    update.message.reply_text(f"Вы сказали: {update.message.text}")

# Добавление обработчиков команд
dispatcher.add_handler(CommandHandler("start", start))
dispatcher.add_handler(CommandHandler("help", help))
dispatcher.add_handler(CommandHandler("signal", trade_signal))
dispatcher.add_handler(CommandHandler("status", trade_status))
dispatcher.add_handler(CommandHandler("buttons", button))

# Добавление обработчика нажатий на кнопки
dispatcher.add_handler(CallbackQueryHandler(button_handler))

# Обработчик сообщений
dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

# Запуск бота
updater.start_polling()
updater.idle()
