from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
from app.api.v1 import endpoints, auth, analytics, signals, telegram_bot
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from app.middleware.audit import AuditMiddleware
from app.monitoring.metrics import MetricsMiddleware
import sentry_sdk
from sentry_sdk.integrations.fastapi import FastApiIntegration
from prometheus_fastapi_instrumentator import Instrumentator
import os
import logging
from app.utils import check_database_status, check_redis_status
from app.cache.redis_cache import cache
import time

# Initialize Sentry
sentry_sdk.init(
    dsn=os.getenv("SENTRY_DSN"),
    integrations=[FastApiIntegration()],
    traces_sample_rate=1.0,
    environment=os.getenv("ENVIRONMENT", "development")
)

# Initialize rate limiter
limiter = Limiter(key_func=get_remote_address)
app = FastAPI()
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        os.getenv("FRONTEND_URL", "https://your-production-domain.com"),
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Add compression middleware
app.add_middleware(GZipMiddleware, minimum_size=1000)

# Add audit middleware
app.add_middleware(AuditMiddleware)

# Add metrics middleware
app.add_middleware(MetricsMiddleware)

# Initialize Prometheus metrics
Instrumentator().instrument(app).expose(app)

# Настроим логирование
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('app.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# Используем безопасные хосты
app.add_middleware(TrustedHostMiddleware, allowed_hosts=[os.getenv("ALLOWED_HOST", "*")])

@app.get("/status")
@limiter.limit("5/minute")
@cache.cached(ttl=60)  # Cache for 1 minute
async def system_status():
    """Проверка статуса API, базы данных и Redis"""
    logger.info("Checking system status")
    db_status = check_database_status()
    redis_status = check_redis_status()
    
    if db_status and redis_status:
        return {"status": "Healthy"}
    logger.error(f"System unhealthy: DB={db_status}, Redis={redis_status}")
    return {"status": "Unhealthy", "db": db_status, "redis": redis_status}

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

@app.on_event("startup")
async def startup_event():
    logger.info("Application starting up...")
    # Здесь можно добавить инициализацию подключений к базе данных,
    # кэшу и другим сервисам

@app.on_event("shutdown")
async def shutdown_event():
    logger.info("Application shutting down...")
    # Здесь можно добавить закрытие подключений к базе данных,
    # кэшу и другим сервисам
