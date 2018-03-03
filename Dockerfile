FROM tensorflow/tensorflow
MAINTAINER andrey@yashchak.ru

RUN mkdir -p /app
WORKDIR /app
RUN pip install -r requirements.txt
RUN ls -la
