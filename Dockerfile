FROM python:3.8.14-slim

ARG API_KEY
ARG DB_USER
ARG DB_PASSWORD
ARG DB_HOST
ARG DB_PORT
ARG DB_NAME

WORKDIR /main_app

COPY requirements.txt .

RUN python -m pip install --upgrade pip setuptools wheel
RUN pip install --root-user-action=ignore -r requirements.txt

ADD app/ .

ENV API_KEY=$API_KEY
ENV DB_USER=$DB_USER
ENV DB_PASSWORD=$DB_PASSWORD
ENV DB_HOST=$DB_HOST
ENV DB_PORT=$DB_PORT
ENV DB_NAME=$DB_NAME

CMD ["python", "weather.py"]