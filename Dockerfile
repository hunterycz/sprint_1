FROM python:3

ENV PYTHONUNBUFFERED=1

RUN apt-get update
RUN apt-get upgrade -y
RUN pip install --upgrade pip
RUN pip install pandas numpy