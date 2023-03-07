import argparse
from kafka import KafkaConsumer
from producer import result
import json
import sys
import ast

def consumer(bootstrapServers, consumerTopicName, producerTopicName):
   
    conf = {
        'bootstrap_servers': [bootstrapServers],
        'topic_name': consumerTopicName,
    }

    # print(conf['bootstrap_servers'])
    # print(conf['topic_name'])
    # print(producerTopicName)

    print('start consumer')
    consumer = KafkaConsumer(conf['topic_name'],
                            bootstrap_servers=conf['bootstrap_servers'],  group_id='consumer_id')

    for message in consumer:
        data = message.value 
        print(data)
        # data = json.loads(data)
        
        print(type(data))
        result(json.loads(data),bootstrapServers, producerTopicName)

    print('end consumer')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-b', '--bootstrap_servers', type=str,
                        help='bootstrap servers')
    parser.add_argument('-c', '--consumer_topic_name', type=str,
                        help='consumer topic name')
    parser.add_argument('-p', '--producer_topic_name', type=str,
                        help='producer topic name')


    args = parser.parse_args()
   

    consumer(args.bootstrap_servers,args.consumer_topic_name,args.producer_topic_name)