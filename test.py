from kafka import KafkaConsumer
from producer import result
import json
import sys

conf = {
    'bootstrap_servers': ["172.16.10.95:9092"],
    'topic_name': 'kafka-received-detect-link-aloline',
    'consumer_id': 'consumer-id'
}

print('start test')
consumer = KafkaConsumer(conf['topic_name'],
                        bootstrap_servers=conf['bootstrap_servers'],  group_id=conf['consumer_id'])

for message in consumer:
    #print("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,message.offset, message.key,message.value))
    topic = message.topic
    data = message.value
    print(topic)
    print(data)
    print(type(data))
    # {
    #     "object_id": "123",
    #     "type": 0,
    #     "link": ["abc.com", "xyz.vn"]
    # }

print('end test')