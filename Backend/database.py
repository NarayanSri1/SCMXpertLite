from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

try:
    conn=MongoClient("mongodb://localhost:27017")
    db = conn.SCMXpert
    try: 
       db.command("serverStatus")
    except ConnectionFailure as e: 
        print("Failed Connection..."+repr(e))
    else: print("Database Connected...")
except Exception as e:
  print(repr(e))
