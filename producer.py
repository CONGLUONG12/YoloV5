from kafka import KafkaProducer
from main import detect
import json


def result(contents, bootstrapServers, producerTopicName):
# Define server with port
    conf = {
        'bootstrap_servers': [bootstrapServers],
        'topic_name': producerTopicName,
    }

    print('start producer')
        
    producer = KafkaProducer(bootstrap_servers=conf['bootstrap_servers'], key_serializer=str.encode, value_serializer=str.encode)
         
    result = detect(contents=contents)
    
    # Publish text in defined topic
    # producer.send(conf['topic_name'], key="abc", value=json.dumps(result))
    # result = '{"object_id": "123", "status": 200, "message": "OK", "data": [{"link_hinh": "https://live.staticflickr.com/65535/49932658111_30214a4229_b.jpg", "status": 1}, {"link_hinh": "https://cute18x.com/wp-content/uploads/2022/06/anh-khoa-than-goi-duc-khong-che-nude-dep-ngat-ngay-1.jpg", "status": 0}]}'
    producer.send(conf['topic_name'], key="abc", value=str(result))
    producer.close()
    print('end producer')

