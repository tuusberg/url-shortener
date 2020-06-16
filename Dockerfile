FROM python:3.8.3

WORKDIR app

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY * ./

EXPOSE 8080

CMD bin/app.py
