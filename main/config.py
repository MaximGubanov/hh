import os

from dotenv import load_dotenv


class Config:

    def __init__(self):

        dotenv_path = os.path.join(os.path.dirname(__file__), '.env')

        if os.path.exists(dotenv_path):
            load_dotenv(dotenv_path)
            env = os.environ

            self.BASE_URL = 'https://api.hh.ru/'
            self.AUTH_URL = 'https://hh.ru/oauth/token'
            self.UTF = 'utf-8'
            self.QUERY_INTERVAL = 1800

            self.HEADERS = {
                'User Agent':
                    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) '
                    'Chrome/103.0.0.0 Safari/537.36',
                'Content-Type': 'application/x-www-form-urlencoded',
            }

            self.DATA = {
                'grant_type': env['GRANT_TYPE'],
                'client_id': env['CLIENT_ID'],
                'client_secret': env['CLIENT_SECRET'],
            }
