import argparse

bootstrapServers = ''
consumerTopicName = ''
producerTopicName = ''
# def convert_enviroment(bootstrapServers, consumerTopicName, producerTopicName):
#     return bootstrapServers, consumerTopicName, producerTopicName
def convert_enviroment():
    return bootstrapServers, consumerTopicName, producerTopicName

if __name__ == '__main__':
    print(11111111111)
    parser = argparse.ArgumentParser()
    parser.add_argument('-b', '--bootstrap_servers', type=str,
                        help='bootstrap servers')
    parser.add_argument('-c', '--consumer_topic_name', type=str,
                        help='consumer topic name')
    parser.add_argument('-p', '--producer_topic_name', type=str,
                        help='producer topic name')


    args = parser.parse_args()
    print(args)

    # convert_enviroment(args.bootstrap_servers,args.consumer_topic_name,args.producer_topic_name)
    bootstrapServers = args.bootstrap_servers
    consumerTopicName = args.consumer_topic_name
    producerTopicName = args.producer_topic_name