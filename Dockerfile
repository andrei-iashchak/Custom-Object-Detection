FROM tensorflow/tensorflow
MAINTAINER andrey@yashchak.ru

RUN mkdir -p /app
WORKDIR /app

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY . ./

EXPOSE 5000

ENTRYPOINT ["sh", "/app/start.sh"]
