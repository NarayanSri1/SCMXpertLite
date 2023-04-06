# importing HTTPexception
from fastapi import HTTPException
from models import user, ship
import re

def validation(User:user):
    # assigning password variables
    password_regex="((?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[\W]).{3,20})"
    user_password=User.password
    compile_pass=re.compile(password_regex)
    search=re.search(compile_pass,user_password)

    if not search:
        raise HTTPException(
            status_code=400,detail="Password doesn't follow pattern."
        )
    return search

def shipvalidation(Ship:ship):
    s1 = Ship.Shipment_Invoice_Number
    s2 = Ship.Container_Number
    s3 = Ship.Shipment_Description
    s4 = Ship.Route_Details
    s5 = Ship.Goods_Type
    s6 = Ship.Device
    s7 = Ship.Expected_Delivery_Date
    s8 = Ship.PO_Number
    s9 = Ship.Delivery_Number
    s10 = Ship.NDC_Number
    s11 = Ship.Batch_ID
    s12= Ship.Serial_Number_of_goods
    if(s1 == "" or
       s2 == "" or
       s3 == "" or
       s4 == "" or
       s5 == "" or
       s6 == "" or
       s7 == "" or
       s8 == "" or
       s9 == "" or
       s10 == "" or
       s11 == "" or
       s12 == ""):
        raise HTTPException(
            status_code=400,
            detail= "Please enter the required fields!"
        )