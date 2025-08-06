# Use official Python image
FROM python:3.10-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /usr/src/app

RUN apt-get update && apt-get install -y netcat-openbsd

# Install dependencies
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy project files
COPY . .

# Copy startup script
COPY start.sh /start.sh
RUN chmod +x start.sh && chmod 777 start.sh

# Default command
CMD sh start.sh

