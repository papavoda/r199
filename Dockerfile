# Pull base image
FROM python:3.11-alpine

# Set environment variables
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# set work directory
WORKDIR /code

# Install dependencies
COPY ./requirements.txt .
RUN pip install -r requirements.txt
COPY ./uget_to_get.txt /usr/local/lib/python3.11/site-packages/snowpenguin/django/recaptcha3/fields.py
# Copy project
COPY . .