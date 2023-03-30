from typing import Optional
# include Basemodel classes
from pydantic import BaseModel

# creating a basemodel class
class user(BaseModel):
    username: str
    emailid: str
    password: str
    # confirmpassword: str

class login(BaseModel):
    emailid: str
    password: str

# creating Token Basemodel class
class Token(BaseModel):
    access_token: str
    token_type: str

# creating TokenData Basemodel class
class TokenData(BaseModel):
    username: Optional[str] = None

# creating Shipment class
class ship(BaseModel):
    Shipment_Invoice_Number: str
    Container_Number : str
    Shipment_Description : str
    Route_Details :str
    Goods_Type: str
    Device :str
    Expected_Delivery_Date : str
    PO_Number :str
    Delivery_Number :str
    NDC_Number : str
    Batch_ID :str
    Serial_Number_of_goods:str

# creating Device Data Basemodel class
class devicedata(BaseModel):
    Battery_Level: int
    Device_ID: int
    First_Sensor_Temperature: int
    Route_From: str
    Route_To: str

# creating model dictionary
def userEntity(user) -> dict:
    return{
        "username": str(user["username"]),
        "emailid": str(user["emailid"]),
        "password": str(user["password"]),
        # "cpassword":str(item["cpassword"])
    }

def shipEntity(ship) -> dict:
     return {
        "Shipment_Invoice_Number": str(ship["Shipment_Invoice_Number"]),
        "Container_Number" : str(ship["Container_Number"]),
        "Shipment_Description" : str(ship["Shipment_Description"]),
        "Route_Details" :str(ship["Route_Details"]),
        "Goods_Type" :str(ship["Goods_Type"]),
        "Device" :str(ship["Device"]),
        "Expected_Delivery_Date" : str(ship["Expected_Delivery_Date"]),
        "PO_Number" :str(ship["PO_Number"]),
        "Delivery_Number" :str(ship["Delivery_Number"]),
        "NDC_Number" : str(ship["NDC_Number"]),
        "Batch_ID" :str(ship["Batch_ID"]),
        "Serial_Number_of_goods" :str(ship["Serial_Number_of_goods"]),
          }

def ddEntity(devicedata) -> dict:
    return{
        "Battery_Level":int(devicedata["Battery_Level"]),
        "Device_ID": int(devicedata["Device_ID"]),
        "First_Sensor_Temperature": int(devicedata["First_Sensor_Temperature"]),
        "Route_From": str(devicedata["Route_From"]),
        "Route_To": str(devicedata(["Route_To"]))
    }

# def serializeDict(a) -> dict:
#     return {**{i:str(a[i]) for i in a if i=='_id'},**{i:a[i] for i in a if i!='_id'}}

# def serializeList(entity) -> list:
#     return [serializeDict(a) for a in entity]


           