from fastapi import APIRouter
from app.services.blockchain_integration import get_trade_data
from app.utils import get_trade_data_with_cache

router = APIRouter()

@router.get("/reports/{pair}")
async def generate_report(pair: str):
    cached_data = await get_trade_data_with_cache(pair)
    return cached_data

@router.get("/historical-data")
async def get_historical_data():
    # Пример данных для графика
    return [
        {"date": "2023-10-01", "price": 100},
        {"date": "2023-10-02", "price": 105},
        {"date": "2023-10-03", "price": 110},
    ]