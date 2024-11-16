FROM python:3.11-slim

WORKDIR /app

COPY first_flask.py /app/
COPY config.json /app/
COPY requirements.txt /app/
COPY printcolors.py /app/

RUN pip install -r requirements.txt

EXPOSE 80

CMD ["python", "first_flask.py"]
