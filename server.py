from kafka import KafkaProducer
import json

conf = {
    'bootstrap_servers': ["172.16.10.95:9092"],
    'topic_name': 'kafka-send-detect-link-aloline',
    'consumer_id': 'consumer-id'
}

print('start producer')
producer = KafkaProducer(bootstrap_servers=conf['bootstrap_servers'], key_serializer=str.encode, value_serializer=str.encode)

data = '{"object_id": "123", "type": 0, "link": ["https://live.staticflickr.com/65535/49932658111_30214a4229_b.jpg", "https://cute18x.com/wp-content/uploads/2022/06/anh-khoa-than-goi-duc-khong-che-nude-dep-ngat-ngay-1.jpg"]}'
producer.send(conf['topic_name'], key="abc", value = data)
producer.close()
print('end producer')