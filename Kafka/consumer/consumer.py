import json
import sys
from models import Device_Data
from pymongo import MongoClient
from kafka import KafkaConsumer
from Backend.config import topicName
# import urllib.parse


# username = urllib.parse.quote_plus('Narayan')
# password = urllib.parse.quote_plus("Test@12345")

# url = "mongodb+srv://{}:{}@scmexpert.u5bh017.mongodb.net/?retryWrites=true&w=majority".format(username, password)
# client=MongoClient(url)

client=MongoClient("mongodb://localhost:27017")
db=client["SCMXpert"]
col3=db["Device_Data_Stream"]


bootstrap_servers = "localhost:9092"
# bootstrap_servers = "kafka-kafka-1:9092"


# def ddEntity(Device_Data) -> dict:
#     return{
#         "Battery_Level":str(Device_Data["Battery_Level"]),
#         "Device_ID": str(Device_Data["Device_ID"]),
#         "First_Sensor_Temperature": str(Device_Data["First_Sensor_Temperature"]),
#         "Route_From": str(Device_Data["Route_From"]),
#         "Route_To": str(Device_Data(["Route_To"]))
#     }

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
        col3.insert_one(dict(Transport_Data))
        print(Transport_Data)

except KeyboardInterrupt:
    sys.exit()


# try:
#     consumer = KafkaConsumer(topic_name, 
#                              bootstrap_servers = bootstrap_servers,
#                              auto_offset_reset = 'latest')
    
#     for data in consumer:
#         try:
#             data = json.loads(data.value)
#             metadata = col3.insert_one(data)

#         except json.decoder.JSONDecodeError:
#             continue

# except KeyboardInterrupt:
#     sys.exit()