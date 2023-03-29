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
    if(s1 == ""):
        raise HTTPException(
            status_code=400,
            detail= "Please enter the required field!"
        )