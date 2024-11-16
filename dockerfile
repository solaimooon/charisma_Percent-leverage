From python:3.9


ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


RUN mkdir /backend
WORKDIR /backend
COPY requrments.txt /backend/
RUN pip install -r requrments.txt

COPY . /backend/

RUN python manage.py makemigrations