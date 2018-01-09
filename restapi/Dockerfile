FROM python:3.6-slim

WORKDIR /app

ADD . .

RUN python3 -m pip install -r requirements.txt

EXPOSE 80

ENV FLASK_DEBUG=1

CMD ["python3", "app.py"]