FROM python:3.10.7

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt