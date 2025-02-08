import requests

class BlockchainAPI:
    def __init__(self, base_url):
        self.base_url = base_url

    def get_transactions(self, pair: str):
        url = f"{self.base_url}/transactions/{pair}"
        response = requests.get(url)
        return response.json()

    def get_pair_data(self, pair: str):
        url = f"{self.base_url}/pairs/{pair}"
        response = requests.get(url)
        return response.json()

# Интеграция с Uniswap, Sushiswap и Pancakeswap
uniswap_api = BlockchainAPI("https://api.uniswap.org/v1")
sushiswap_api = BlockchainAPI("https://api.sushi.com/v1")
pancakeswap_api = BlockchainAPI("https://api.pancakeswap.info/api/v2")

# Функция для получения данных с нескольких платформ
def get_trade_data(pair: str):
    uniswap_data = uniswap_api.get_pair_data(pair)
    sushiswap_data = sushiswap_api.get_pair_data(pair)
    pancakeswap_data = pancakeswap_api.get_pair_data(pair)
    return {
        "uniswap": uniswap_data,
        "sushiswap": sushiswap_data,
        "pancakeswap": pancakeswap_data
    }
