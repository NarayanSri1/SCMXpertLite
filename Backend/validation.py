# importing HTTPexception
from fastapi import HTTPException
from models import user, ship
from config import shipment
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
    shipment_invoice_number = Ship.Shipment_Invoice_Number
    container_number = Ship.Container_Number
    description = Ship.Shipment_Description
    route_details = Ship.Route_Details
    goods_type = Ship.Goods_Type
    device_id = Ship.Device
    delivery_date = Ship.Expected_Delivery_Date
    po_number = Ship.PO_Number
    delivery_number = Ship.Delivery_Number
    ndc_number = Ship.NDC_Number
    batch_id = Ship.Batch_ID
    sno_of_goods = Ship.Serial_Number_of_goods

    shipment_check=shipment.find_one({"Shipment_Invoice_Number":shipment_invoice_number})
    if shipment_check:
        raise HTTPException(
            status_code=400,detail="Shipment already exists."
        )

    if(shipment_invoice_number == "" or
       container_number == "" or
       description == "" or
       route_details == "" or
       goods_type == "" or
       device_id == "" or
       delivery_date == "" or
       po_number == "" or
       delivery_number == "" or
       ndc_number == "" or
       batch_id == "" or
       sno_of_goods == ""):
        raise HTTPException(
            status_code=400,
            detail= "Please enter the required fields!"
        )
    
    if not (shipment_invoice_number.isnumeric()):
        raise HTTPException(
            status_code=400,
            detail= "Shipment number should only be alphanumeric."
        )
    
    if (len(description)>120):
        raise HTTPException(
            status_code=400,
            detail= "Please enter the description within 120 characters."
        )
    
    if (len(po_number)!=6):
        raise HTTPException(
            status_code=400,
            detail= "PO Number should be a number of six digits."
        )
    
    