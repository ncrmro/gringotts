import requests

from src import settings
from src.api_adapters import BaseClientAdapter


class TeamUpClient(BaseClientAdapter):
    def __init__(self):
        api_key = settings.TEAMUP_API_KEY
        super().__init__(api_key)

        self.base_url = 'https://api.teamup.com'

    def make_request(self, url):
        headers = {'Teamup-Token': self.api_key}
        request = requests.get(url, headers=headers)
        return request

    def get_access(self):
        url = self.construct_url(self.base_url, '/check-access')
        request = self.make_request(url)
        return request

