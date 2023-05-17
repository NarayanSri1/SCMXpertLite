#establish connection between Python and Mongo
import os
from dotenv import load_dotenv
from pymongo import MongoClient
import urllib.parse

load_dotenv(dotenv_path=".env")

username = urllib.parse.quote_plus(os.getenv("databaseusername"))
password = urllib.parse.quote_plus(os.getenv("databasepassword"))

url = os.getenv("databaseurl").format(username,password)
# connection_string="mongodb://localhost:27017"

client=MongoClient(url)
# client=MongoClient(connection_string)

#Creating DB
database=client["SCMXpert"]

#Creating collections
users= database["Users"]
shipment= database["Shipment"]
device_data_stream= database["Device_Data_Stream"]
