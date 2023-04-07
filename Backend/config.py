#establish connection between Python and Mongo
from pymongo import MongoClient

connection_string="mongodb://localhost:27017"
client=MongoClient(connection_string)

#Creating DB
db=client["SCMXpert"]

#Creating collections
col1=db["Users"]
col2=db["Shipment"]
col3=db["Device_Data_Stream"]

