FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .

RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

COPY . .
CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:8000"]
