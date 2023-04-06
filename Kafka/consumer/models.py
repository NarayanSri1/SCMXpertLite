# from mongoengine import DynamicDocument, IntField, StringField
from pydantic import BaseModel

# class Device_data(DynamicDocument):
#     Battery_Level = IntField()
#     Device_Id = IntField()
#     First_Sensor_temperature = IntField()
#     Route_From = StringField()
#     Route_To = StringField()  

class Device_Data(BaseModel):
    Battery_Level: int
    Device_ID: int
    First_Sensor_Temperature: int
    Route_From: str
    Route_To: str