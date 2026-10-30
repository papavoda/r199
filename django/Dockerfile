# syntax=docker/dockerfile:1
# Pull base image
FROM python:3.14-alpine
# Set environment variables
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


# set work directory
WORKDIR /code

# Install dependencies
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# Copy project
#COPY . .
#EXPOSE 8000
#
#ENTRYPOINT ["python", "manage.py", "runserver"]
#CMD ["0.0.0.0:8000"]

