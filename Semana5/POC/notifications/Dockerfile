FROM python:3.8-slim
WORKDIR /app
COPY requirements.txt .
RUN apt-get update && \
    apt-get install -y build-essential && \
    apt-get install -y libpq-dev && \
    pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["python", "notification_service.py"]
