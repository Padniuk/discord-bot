FROM python:3.10.9

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

RUN apt-get update && apt-get install -y ffmpeg

COPY . .

WORKDIR /app/bot

CMD ["python3", "main.py"]
