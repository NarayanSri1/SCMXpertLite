# routes the fastapi with functionalitites
from fastapi import APIRouter, HTTPException, Depends
from models import user, ship, login, Device_Data, userEntity, ddEntity, forgotpwd
from utils import Hash
from validation import validation, shipvalidation
from bson import json_util
import json
# import function from other user defined python files
# from database import conn
from jwt import create_access_token, get_current_user
from config import col1, col2, col3

# routing variable
add=APIRouter()

# Register user via Sign-in Page
@add.post('/signup')
async def create_user(Signup: user):
    email_check=col1.find_one({"emailid":Signup.emailid})
    validation(Signup)
    if email_check:
        raise HTTPException(
            status_code=400,detail="User already exists."
        )
    else:
        hashed_pass=Hash.hash_password(Signup.password)
        Signup.password=hashed_pass
        col1.insert_one(dict(Signup))
    # this returns the user created --return (create_user)
    return {"Registered Successfully"}

# Login Page validation
@add.post('/login')
async def find_user(Login:login):
    user_data=col1.find_one({"emailid":Login.emailid})
    if not user_data:
        raise HTTPException(
            status_code=400,detail="Email not found."
        )
    if not Hash.verify_password(Login.password,user_data["password"]):
        raise HTTPException(
            status_code=400, detail="Incorrect Password."
        )    
    access_token = create_access_token(data={"token":user_data["emailid"]})
    return{"access_token":access_token,"token_type":"bearer"}

# The self parameter is a reference to the current instance of the class, 
# and is used to access variables that belongs to the class.

@add.get('/forgotpwd')
async def find_user(Fwt:forgotpwd):
    user_data=col1.find_one({"emailid":Fwt.emailid})
    if not user_data:
        raise HTTPException(
            status_code=400,detail="Email not found."
        )
    else:
        return {'message': 'Redirect to Reset Password'}

@add.put('/resetpwd')
async def find_user(Fwt:login):
          hashed_pass=Hash.hash_password(Fwt.password)
          Fwt.password=hashed_pass
          data = dict(Fwt)
          col1.find_one_and_update({"emailid":Fwt.emailid}, {'$set': data})
          print(Fwt.password)
          return {'message': 'Password Updated'}

    # Return a success message
    # return {'message': 'Todo updated successfully'}

    #     Fwt.emailid = Signup.emailid
    #     hashed_pass=Hash.hash_password(Signup.password)
    #     Signup.password=hashed_pass
    #     data = Signup.password
    #     updated_password =  col1.update_one(
    #     {"emailid":Signup.emailid}, {"$set": data}
    # )
    # return {"Password Reset":updated_password} 
  

@add.get('/dashboard')
async def redirect(token:str=Depends(get_current_user)):
    if token:
        return True

# Import data from shipments page
@add.post('/shipment')
async def create_shipment(Shipment: ship, token:str=Depends(get_current_user)):
    if token:
        shipvalidation(Shipment)
        col2.insert_one(dict(Shipment))
        return {"Shipment Created!"}
    else:
        raise HTTPException(
            status_code=401, detail='Unauthorized Entry'
            )

@add.get('/getusers')
def get_users():
    users = []
    docs = col1.find({})
    for user in docs:
        users.append(userEntity(user))
    return users

@add.get('/devicedata')
def get_devicedata(token:str=Depends(get_current_user)):
    if token:
        data = col3.find({},{"_id":0})
        response = json.loads(json_util.dumps(data))
        return response
    else:
        raise HTTPException(
            status_code=401, detail='Unauthorized Access'
        )
    


    
