# routes the fastapi with functionalitites
from fastapi import APIRouter, HTTPException, Depends
from models import user, ship, login, userEntity, forgotpwd
from utils import Hash
from validation import validation, shipvalidation
from bson import json_util
import json
# import function from other user defined python files
# from database import conn
from jwt import create_access_token, get_current_user
from config import users, shipment, device_data_stream

# routing variable
add=APIRouter()

# Register user v
# ia Sign-in Page
@add.post('/signup')
async def create_user(Signup: user):
    email_check=users.find_one({"emailid":Signup.emailid})
    validation(Signup)
    if email_check:
        raise HTTPException(
            status_code=400,detail="User already exists."
        )
    else:
        hashed_pass=Hash.hash_password(Signup.password)
        Signup.password=hashed_pass
        users.insert_one(dict(Signup))
    # this returns the user created --return (create_user)
    return {"Registered Successfully"}

# Login Page validation
@add.post('/login')
async def find_user(Login:login):
    user_data=users.find_one({"emailid":Login.emailid})
    if not user_data:
        raise HTTPException(
            status_code=400,detail="Email not found."
        )
    if not Hash.verify_password(Login.password,user_data["password"]):
        raise HTTPException(
            status_code=400, detail="Incorrect Password."
        )    
    access_token = create_access_token(data={"token":user_data["username"], "role":user_data["role"]})
    return{"access_token":access_token,"token_type":"bearer"}

# The self parameter is a reference to the current instance of the class, 
# and is used to access variables that belongs to the class.

# Api for forgot password flow
@add.post('/forgotpwd')
async def find_user(Fwt:forgotpwd):
    user_data=users.find_one({"emailid":Fwt.emailid})
    if not user_data:
        raise HTTPException(
            status_code=400,detail="Email not found."
        )
    else:
        return {'emailid':user_data["emailid"],'message': 'Redirect to Reset Password'}

@add.put('/resetpassword')
async def find_user(Fwt:login):
          hashed_pass=Hash.hash_password(Fwt.password)
          Fwt.password=hashed_pass
          data = dict(Fwt)
          users.find_one_and_update({"emailid":Fwt.emailid}, {'$set': data})
          print(Fwt.password)
          return {'message': 'Password Updated'}

# Dashboard API containing the token as local storage
@add.get('/dashboard')
async def redirect(token:str=Depends(get_current_user)):
    if token:
        return {"response":token}

# Post Data to shipment db in Mongo
@add.post('/shipment')
async def create_shipment(Shipment: ship, token:str=Depends(get_current_user)):
    if token:
        shipvalidation(Shipment)
        shipment.insert_one(dict(Shipment))
        return {"Shipment Created!"}
    else:
        raise HTTPException(
            status_code=401, detail='Unauthorized Entry'
            )
    
# --get all shipment collection
@add.get('/getShipData')
def get_shipmentdata(token:str=Depends(get_current_user)):
    if token:
        data = shipment.find({},{"_id":0})
        response = json.loads(json_util.dumps(data))
        return response
    else:
        raise HTTPException(
            status_code=401, detail='Unauthorized Access'
        )
# -- get user based shipment collection
@add.get('/usergetShipdata')
def get_usershipmentdata(token:str=Depends(get_current_user)):
    if token:
        data = shipment.find({"user_name":token["token"]})
        response = json.loads(json_util.dumps(data))
        return response
    
    else:
        raise HTTPException(
            status_code=401, detail='Unauthorized Access'
        )


# get users from db
@add.get('/getusers')
def get_users():
    users = []
    docs = users.find({})
    for user in docs:
        users.append(userEntity(user))
    return users

# Get Kafka dds from Mongo 
@add.get('/devicedata')
def get_devicedata(token:str=Depends(get_current_user)):
    if token:
        data = device_data_stream.find({},{"_id":0})
        response = json.loads(json_util.dumps(data))
        return response
    else:
        raise HTTPException(
            status_code=401, detail='Unauthorized Access'
        )