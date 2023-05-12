#establish connection between Python and Mongo
from pymongo import MongoClient
import urllib.parse

username = urllib.parse.quote_plus('Narayan')
password = urllib.parse.quote_plus("Test@12345")

url = "mongodb+srv://{}:{}@scmexpert.u5bh017.mongodb.net/?retryWrites=true&w=majority".format(username, password)

# connection_string="mongodb://localhost:27017"
client=MongoClient(url)

#Creating DB
db=client["SCMXpert"]

#Creating collections
col1=db["Users"]
col2=db["Shipment"]
col3=db["Device_Data_Stream"]

