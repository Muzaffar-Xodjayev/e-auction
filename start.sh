#!/bin/sh

echo "Waiting for PostgreSQL..."

while ! nc -z $DB_HOST $DB_PORT; do
  sleep 1
done

echo "PostgreSQL started"

echo "Applying makemigrations"
python manage.py makemigrations

echo "Applying migrations..."
python manage.py migrate

echo "Collecting static files..."
python manage.py collectstatic --noinput

echo "Starting server..."
gunicorn --workers=4 --threads=2 --bind 0.0.0.0:8000 core.wsgi:application
