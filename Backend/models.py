from enum import Enum
from typing import Optional
# include Basemodel classes
from pydantic import BaseModel

# creating a basemodel class
class user(BaseModel):
    username: str
    emailid: str
    password: str
    role: str
    # confirmpassword: str

class login(BaseModel):
    emailid: str
    password: str

class forgotpwd(BaseModel):
    emailid: str
  

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
class Device_Data(BaseModel):
    Battery_Level: str
    Device_ID: str
    First_Sensor_Temperature: str
    Route_Details: str
    Route_To: str

class Shipment_Data(BaseModel):
    Shipment_Invoice_Number: str
    Device: str
    Goods_Type: str
    Route_Details: str
    Expected_Delivery_Date: str

# creating model dictionary
def userEntity(user) -> dict:
    return{
        "username": str(user["username"]),
        "emailid": str(user["emailid"]),
        "password": str(user["password"]),
        "role":str(user["role"])
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

def ddEntity(Device_Data) -> dict:
    return {
        "Battery_Level":str(Device_Data["Battery_Level"]),
        "Device_ID": str(Device_Data["Device_ID"]),
        "First_Sensor_Temperature": str(Device_Data["First_Sensor_Temperature"]),
        "Route_From": str(Device_Data["Route_From"]),
        "Route_To": str(Device_Data(["Route_To"])),
    }




# to get dictionary to list - to show data to 

# def serializeDict(a) -> dict:
#     return {**{i:str(a[i]) for i in a if i=='_id'},**{i:a[i] for i in a if i!='_id'}}

# def serializeList(entity) -> list:
#     return [serializeDict(a) for a in entity]


           