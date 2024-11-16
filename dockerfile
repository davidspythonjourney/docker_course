FROM python:3.11-slim

WORKDIR /app

COPY first_flask.py /app/
COPY config.json /app/
COPY requirements.txt /app/
copy printcolors.py

RUN pip install -r requirements.txt

EXPOSE 80

CMD ["python", "first_flask.py"]
