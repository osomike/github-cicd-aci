FROM python:3.8.14-slim

ARG API_KEY

WORKDIR /main_app

COPY requirements.txt .

RUN python -m pip install --upgrade pip setuptools wheel
RUN pip install --root-user-action=ignore -r requirements.txt

ADD app/ .

ENV API_KEY=$API_KEY

CMD ["python", "weather.py"]