FROM python:3.9-slim-buster
RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6  -y
RUN mkdir /app
WORKDIR /app
COPY Requirements.txt /app

RUN pip install --upgrade pip
RUN pip install -r Requirements.txt 
COPY . /app
ENTRYPOINT ["python","consumer.py","--b=172.16.10.95:9092","--c=kafka-send-detect-link-aloline","-p=kafka-received-detect-link-aloline"]  
# RUN python consumer.py --b=172.16.10.96:9092 --c=kafka-send-detect-link-aloline -p=kafka-received-detect-link-aloline