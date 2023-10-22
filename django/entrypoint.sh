#!/bin/sh
#python manage.py makemigrations --noinput
#python manage.py migrate --noinput
gunicorn r199.wsgi:application --bind 0.0.0.0:8000
# gunicorn for nginx
# gunicorn --workers 5 --bind unix:/run/gunicorn.sock config.wsgi:application
# python manage.py runserver 0.0.0.0:8000
