# routes the fastapi with functionalitites
from fastapi import APIRouter, HTTPException, Depends
from models import user, ship, login
from utils import Hash
from validation import validation

# import function from other user defined python files
from database import conn
from jwt import create_access_token, get_current_user

# routing variable
add=APIRouter()

# Register user via Sign-in Page
@add.post('/signup')
async def create_user(Signup: user):
    email_check=conn.SCMXpert.Sign_up.find_one({"emailid":Signup.emailid})
    validation(Signup)
    if email_check:
        raise HTTPException(
            status_code=400,detail="Email already exists."
        )
    else:
        hashed_pass=Hash.hash_password(Signup.password)
        Signup.password=hashed_pass
        conn.SCMXpert.Sign_up.insert_one(dict(Signup))
    # return (create_user)
    return {"Registered Successfully"}

# Login Page validation
@add.post('/login')
async def find_user(Login:login):
    user_data=conn.SCMXpert.Sign_up.find_one({"emailid":Login.emailid})
    if not user_data:
        raise HTTPException(
            status_code=400,detail="Email not found"
        )
    if not Hash.verify_password(Login.password,user_data["password"]):
        raise HTTPException(
            status_code=400, detail="Password Mistmatch"
        )    
    access_token = create_access_token(data={"token":user_data["emailid"]})
    return{"access_token":access_token,"token_type":"bearer"}

# The self parameter is a reference to the current instance of the class, 
# and is used to access variables that belongs to the class.

@add.get('/dashboard')
async def redirect(token:str=Depends(get_current_user)):
    if token:
        return True

# Import data from shipments page
@add.post('/shipment')
async def create_shipment(Shipment: ship, token:str=Depends(get_current_user)):
    if token:
        conn.SCMXpert.Shipment.insert_one(dict(Shipment))
        return {"Uploaded Successfully"}
    else:
        raise HTTPException(
            status_code=401, detail='Unauthorized entry'
            )
        
