# import urllib.parse
import os
# from dotenv import load_dotenv
from pymongo import MongoClient

# load_dotenv(dotenv_path=".env")


# username = urllib.parse.quote_plus(os.getenv("databaseusername"))
# password = urllib.parse.quote_plus(os.getenv("databasepassword"))

# databaseurl = "mongodb+srv://{}:{}@scmexpert.u5bh017.mongodb.net/?retryWrites=true&w=majority".format(username, password)

client=MongoClient(os.getenv("databaselocal"))
# client=MongoClient(databaseurl)

database=client["SCMXpert"]
Device_Data_Stream=database["Device_Data_Stream"]
topicName='Device_Data_Stream'