class BaseClientAdapter:
    def __init__(self, api_key):
        self.api_key = api_key

    def initialize(self):
        return self.api_key


    def construct_url(self, base_url, endpoint):
        data = {'base_url': base_url, 'endpoint': endpoint}
        url = '{base_url}{endpoint}'.format(**data)
        return url
