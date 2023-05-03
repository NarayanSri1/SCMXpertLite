import json
import sys
from models import Device_Data
from pymongo import MongoClient
from kafka import KafkaConsumer

# MongoClient(db="SCMXpert", host="localhost", port=27017)
client=MongoClient("mongodb://localhost:27017")
db=client["SCMXpert"]
col3=db["Device_Data_Stream"]

bootstrap_servers = "localhost:9092"
topic_name = 'device_data'


# def ddEntity(Device_Data) -> dict:
#     return{
#         "Battery_Level":str(Device_Data["Battery_Level"]),
#         "Device_ID": str(Device_Data["Device_ID"]),
#         "First_Sensor_Temperature": str(Device_Data["First_Sensor_Temperature"]),
#         "Route_From": str(Device_Data["Route_From"]),
#         "Route_To": str(Device_Data(["Route_To"]))
#     }

try:
    consumer = KafkaConsumer(topic_name, 
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