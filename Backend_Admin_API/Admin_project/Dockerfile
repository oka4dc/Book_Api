# Using the official Python image on dockerhub.
FROM python:3.11

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install necessary system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*
# Set work directory
WORKDIR /usr/src/app

# Install dependencies
COPY requirements.txt /usr/src/app/

RUN pip install --upgrade pip

# Install the required packages
RUN pip install -r requirements.txt

# Copy project
COPY . /usr/src/app/

# make port 8000 available to the outside world
EXPOSE 8000

# Run the Django development server
CMD ["gunicorn", "--bind", "*:8000", "core.wsgi:application"]
