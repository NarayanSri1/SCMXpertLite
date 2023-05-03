# importing HTTPexception
from fastapi import HTTPException
from models import user, ship
from config import col2
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
    shipment_check=col2.find_one({"Shipment_Invoice_Number":s1})

    if shipment_check:
        raise HTTPException(
            status_code=400,detail="Shipment already exists."
        )

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
    
    if not (s1.isnumeric()):
        raise HTTPException(
            status_code=400,
            detail= "Shipment number should only be alphanumeric."
        )
    
    if (len(s3)>120):
        raise HTTPException(
            status_code=400,
            detail= "Please enter the description within 120 characters."
        )
    
    if (len(s8)>6):
        raise HTTPException(
            status_code=400,
            detail= "PO Number should be a number of six digits."
        )
    
    