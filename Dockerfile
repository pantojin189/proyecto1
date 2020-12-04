From python:3.6

MAINTAINER Jesus Jose Gomez Pantoja "gpjesus108@gmail.com"

EXPOSE 5000

WORKDIR /app

copy requirements.txt /app

RUN pip install -r requirements.txt

COPY . /app

CMD python main.py