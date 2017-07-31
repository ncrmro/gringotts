from src import settings
from coinbase.wallet.client import Client
import requests

from src import settings
from src.api_adapters import BaseClientAdapter


class CoinBasClient(BaseClientAdapter):
    def __init__(self):
        api_key = settings.MEETUP_API_KEY
        super().__init__(api_key)
        self.base_url = 'https://api.meetup.com'

    def make_request(self, url):
        payload = {'key': self.api_key}
        request = requests.get(url, params=payload)
        print(request)
        return request

    def get_group(self):
        url = self.construct_url(self.base_url, '/find/groups')
        request = self.make_request(url)
        return request


client = Client(settings.COINBASE_API_KEY, settings.COINBASE_API_KEY)
