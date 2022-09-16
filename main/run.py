from datetime import datetime
from session import Session


if __name__ == '__main__':
    print(f'[ START SESSION {datetime.now().strftime("%Y-%m-%d %H:%M:%S")} ]')

    session = Session()

    data = {
        'text': 'python AND ((drf OR restframework) OR django OR backend)',
        'date_from': datetime.now().strftime("%Y-%m-%dT00:00:00"),
        'area': ['66', '1', '2'],  # поиск по Нижнему Новгороду, Москве и СПб
    }

    session.run(data_to_send=data)
