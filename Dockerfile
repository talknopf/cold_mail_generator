FROM python:3.8-slim-buster

WORKDIR /app
COPY requirements.txt .
COPY . .

RUN python3 -m pip install -r requirements.txt
EXPOSE 80
CMD [ "python3", "/app/email_api.py" ]