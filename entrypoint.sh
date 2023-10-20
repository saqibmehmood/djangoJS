#!/bin/sh

python manage.py migrate

if [ "$APP_INSTANCE" = "web1" ]; then
    # Start the first instance
    python manage.py runserver 0.0.0.0:8000

else
    echo "Unknown application instance"
    exit 1
fi

#  exec daphne Blog.asgi:application --port 8000 --bind 0.0.0.0
#exec daphne Blog.asgi:application --port 8000 --bind 0.0.0.0
#python manage.py runserver 0.0.0.0:8000











