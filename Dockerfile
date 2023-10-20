# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set enviroment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    libpq-dev \
    gcc

# Install Python dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Django project code into container

Copy . /app/

# Expose port 8000 for Django application
Expose 8000

# Start the Django application with Gunicorn
COPY entrypoint.sh /entrypoint.sh
#CMD ["gunicorn", "Blog.wsgi:application", "--bind", "0.0.0.0:8000"]
#CMD ["daphne", "-u", "/tmp/daphne.sock", "Blog.asgi:application"]

#CMD ["daphne", "Blog.asgi:application", "--port", "8000", "--bind", "0.0.0.0"]
ENTRYPOINT ["/entrypoint.sh"]





