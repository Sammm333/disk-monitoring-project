FROM python:3.9-slim

# Установка зависимостей для сборки psutil
RUN apt-get update && apt-get install -y gcc python3-dev && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY disk_monitor.py .

CMD ["python", "disk_monitor.py"]
