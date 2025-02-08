from fastapi import APIRouter
from app.services.blockchain_integration import uniswap_api, sushiswap_api

router = APIRouter()

@router.get("/reports/{pair}")
async def generate_report(pair: str):
    uniswap_data = uniswap_api.get_pair_data(pair)
    sushiswap_data = sushiswap_api.get_pair_data(pair)
    report = {
        "uniswap": uniswap_data,
        "sushiswap": sushiswap_data,
    }
    return report
