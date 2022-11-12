# FROM python:3.10-bullseye
FROM python:3.10-slim-bullseye

ENV PYTHONUNBUFFERED=1
RUN pip install --upgrade pip \
  && echo 'root:Docker!' | chpasswd \
  && useradd -ms /bin/bash backdev

COPY .goodies/.bashrc /home/backdev
WORKDIR /project/backend

COPY src/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

USER backdev
