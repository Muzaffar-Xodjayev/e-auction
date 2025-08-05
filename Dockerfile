# Use official Python image
FROM python:3.10-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /usr/src/app

# Install dependencies
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy project files
COPY . .

# Copy startup script
COPY start.sh /start.sh
RUN chmod +x start.sh

# Default command
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

