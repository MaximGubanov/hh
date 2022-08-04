FROM python:alpine

WORKDIR /app/

ADD . /app/

RUN python -m pip install --upgrade pip

RUN pip install -r requirements.txt

CMD ['python', 'run.py']