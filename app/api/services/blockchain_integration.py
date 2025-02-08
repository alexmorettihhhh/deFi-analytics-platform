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

uniswap_api = BlockchainAPI("https://api.uniswap.org/v1")
sushiswap_api = BlockchainAPI("https://api.sushi.com/v1")
