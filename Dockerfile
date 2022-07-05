FROM python:3.8

RUN apt-get update -y && \
  apt-get install -y python3-pip python3.8-dev

WORKDIR /app

COPY . .

CMD ["python", "main.py"]