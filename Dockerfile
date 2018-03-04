FROM python:3
MAINTAINER andrey@yashchak.ru

RUN mkdir -p /app
WORKDIR /app

COPY requirements.txt ./

RUN pip install -r requirements.txt

RUN which python3
RUN which python

COPY . ./

EXPOSE 5000

RUN protoc object_detection/protos/*.proto --python_out=.
ENV PYTHONPATH=$PYTHONPATH:`pwd`:`pwd`/slim

CMD ["python", "server.py"]
