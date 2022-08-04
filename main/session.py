from time import sleep
from datetime import datetime, timedelta

from config import Config
from request import Request, Token
from bot import bot_send_to_chat


class Session:

    def __init__(self):
        self.config = Config()
        self.token = Token(self.config, url=self.config.AUTH_URL)

    def run(self, data_to_send):
        request = Request(config=self.config)

        try:
            hhtoken, status = self.token()
            while True:
                try:
                    if hhtoken:
                        print(hhtoken, status)
                        vacancies = request.get_data(hhtoken=hhtoken, data=data_to_send)
                        print(vacancies)
                        if vacancies['found'] != 0:
                            for vac in vacancies['items']:
                                if vac['alternate_url']:
                                    print(vac['alternate_url'])
                                    bot_send_to_chat(data=vac['alternate_url'])
                                else:
                                    print(None)
                                    continue
                        else:
                            print('Новых вакансий пока нет')
                        print('Ожидаем новый запрос вакансий... ', datetime.now())
                        sleep(300)
                        period_time = datetime.now() - timedelta(minutes=5)
                        data_to_send['date_from'] = period_time.strftime("%Y-%m-%dT%H:%m:00")
                    else:
                        print('Ожидаем новый токен...')
                        sleep(300)
                        hhtoken = self.token()
                        continue
                except Exception as error:
                    print(error)
                    exit()
        except Exception as error:
            print("Ошибка получения токена: ", error)
