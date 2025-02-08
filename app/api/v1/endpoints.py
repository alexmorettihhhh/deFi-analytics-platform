from fastapi import WebSocket, WebSocketDisconnect
from app.services.blockchain_integration import uniswap_api, sushiswap_api
import json

@router.websocket("/ws/{pair}")
async def websocket_endpoint(websocket: WebSocket, pair: str):
    await websocket.accept()
    while True:
        data = uniswap_api.get_pair_data(pair)
        await websocket.send_text(json.dumps(data))
