FROM tensorflow/tensorflow
MAINTAINER andrey@yashchak.ru

RUN mkdir -p /app
WORKDIR /app

COPY requirements.txt ./
RUN apt-get update && apt-get install python-matplotlib -y

RUN pip install -r requirements.txt

RUN which python3
RUN which python

COPY . ./

EXPOSE 5000

ENTRYPOINT ["sh", "/app/start.sh"]
