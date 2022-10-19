FROM python:3.10.8

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy source code
COPY . .

EXPOSE 8080
# Run the app
CMD ["python", "app.py"]