from fastapi import FastAPI
from app.api.v1 import endpoints, auth, analytics, signals, telegram_bot
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from telegram_bot import send_telegram_message
from fastapi.responses import JSONResponse
import os
import logging
from app.utils import check_database_status, check_redis_status
import time

app = FastAPI()

# Настроим логирование
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(message)s")

# Используем безопасные хосты
app.add_middleware(TrustedHostMiddleware, allowed_hosts=[os.getenv("ALLOWED_HOST", "*")])

@app.get("/status")
async def system_status():
    """Проверка статуса API, базы данных и Redis"""
    db_status = check_database_status()
    redis_status = check_redis_status()
    
    if db_status and redis_status:
        return JSONResponse(content={"status": "Healthy"}, status_code=200)
    return JSONResponse(content={"status": "Unhealthy", "db": db_status, "redis": redis_status}, status_code=500)

@app.get("/trade/{pair}")
async def get_trade(pair: str):
    """Получение торговых данных с кэшированием"""
    data = await get_trade_data_with_cache(pair)
    return data

# Подключаем все роутеры
app.include_router(auth.router)
app.include_router(endpoints.router)
app.include_router(analytics.router)
app.include_router(signals.router)
app.include_router(telegram_bot.router)
