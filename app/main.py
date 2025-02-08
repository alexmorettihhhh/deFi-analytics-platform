from fastapi import FastAPI
from app.api.v1 import endpoints, auth, analytics, signals, telegram_bot
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from telegram_bot import send_telegram_message
app = FastAPI()

# Используем безопасные хосты
app.add_middleware(TrustedHostMiddleware, allowed_hosts=["*"])

def send_trade_signal(signal: str, chat_id: str):
    send_telegram_message(chat_id, signal)
    
@app.get("/trade/{pair}")
async def get_trade(pair: str):
    data = get_trade_data(pair)
    return data

# Подключаем все роутеры
app.include_router(auth.router)
app.include_router(endpoints.router)
app.include_router(analytics.router)
app.include_router(signals.router)
app.include_router(telegram_bot.router)
