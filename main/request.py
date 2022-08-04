import json

import requests


class Request:

    def __init__(self, config):
        self.config = config
        self.base_url = self.config.BASE_URL
        self.headers = self.config.HEADERS
        self.data = self.config.DATA

    def get_data(self, hhtoken, data):
        try:
            self.headers['hhtoken'] = hhtoken
            if hhtoken:
                response = requests.get(url=self.base_url + 'vacancies',
                                        headers=self.headers,
                                        data=data)
                response = json.loads(response.content)
                return response
        except Exception as error:
            print(error)
        return None


class Token(Request):

    def __init__(self, config, url):
        super(Token, self).__init__(config)
        self.url = url
        self.data = config.DATA

    def __call__(self, *args, **kwargs):
        response = requests.post(url=self.url, headers=self.headers, data=self.data)
        if response.status_code == 200:
            return response.content.decode(self.config.UTF), response.status_code
        return False
