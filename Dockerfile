FROM python:3.8-slim-buster
WORKDIR /code
ADD ./docker-scripts.sh /code/docker-scripts.sh
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED=1
COPY requirements_docker.txt .
COPY requirements.txt .
COPY requirements_dev.txt .
RUN pip3 install --upgrade pip && pip3 install -r requirements_docker.txt
ADD . .
RUN python manage.py migrate
