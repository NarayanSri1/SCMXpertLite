from json import loads
from kafka import KafkaConsumer

topic_name='signupusers'

consumer = KafkaConsumer(
    topic_name,
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset = 'earliest',
    enable_auto_commit = True,
    group_id = 'groupusers',
    value_deserializer = lambda x: loads(x.decode('utf-8'))
)
print ("consuming messages")

for message in consumer:
   print('messages: ', message)