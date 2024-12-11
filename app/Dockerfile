# base image
FROM python:3.12-slim

# add a work directory
WORKDIR /app

# env
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1

# install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc libpq-dev && rm -rf /var/lib/apt/lists/*

# install python dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /app
RUN pip install --no-cache-dir -r requirements.txt

# copy files to the container folder
COPY . /app

# start the server
CMD ["uvicorn", "main:main_app", "--host", "0.0.0.0", "--port", "8000"]