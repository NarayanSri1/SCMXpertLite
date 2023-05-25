import json
import sys
from models import Device_Data
from kafka import KafkaConsumer
from config import topicName, Device_Data_Stream


bootstrap_servers = "localhost:9092"
# bootstrap_servers = "backend-kafka-1:9092"
# bootstrap_servers = "root-kafka-1:9092"


try:
    consumer = KafkaConsumer(topicName, 
                             bootstrap_servers = bootstrap_servers,
                             auto_offset_reset = 'latest')
    
    for data in consumer:
        data = json.loads(data.value)
        Transport_Data = Device_Data(
            Battery_Level= data["Battery_Level"],
            Device_ID= data["Device_ID"],
            First_Sensor_Temperature= data["First_Sensor_Temperature"],
            Route_From= data["Route_From"],
            Route_To= data["Route_To"]
        )
        Device_Data_Stream.insert_one(dict(Transport_Data))
        print(Transport_Data)

except KeyboardInterrupt:
    sys.exit()

