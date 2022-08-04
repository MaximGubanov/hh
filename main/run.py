from datetime import datetime
from session import Session


if __name__ == '__main__':

    session = Session()

    data = {
        'text': 'Python, Django, DRF',
        'date_from': datetime.now().strftime("%Y-%m-%dT00:00:00"),
        'area': ['66'],
    }

    session.run(data_to_send=data)
