# Use official Python base image
FROM python:3.10-slim

# Set work directory
WORKDIR /app

# Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy source code
COPY . .

# Required for testing
ENV PYTHONPATH=/app

# Expose port and run app
EXPOSE 5000
CMD ["python", "main.py"]

#docker build -t multi-vehicle-api .
#docker run -p 5000:5000 multi-vehicle-api
#or
#docker-compose up --build
#docker-compose build
#docker-compose run api pytest