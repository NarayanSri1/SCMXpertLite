from fastapi import Depends
from datetime import timedelta, datetime
from jose import jwt # serializeList, serializeDict
from fastapi.security import OAuth2PasswordBearer

# assigning variables for JWT
SECRET_KEY = "my-secret"
ACCESS_TOKEN_EXPIRE_MINUTES = 15
ALGORITHM = "HS256"
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# assigning functions for creation and verification of tokens
def create_access_token(data:dict):
    to_encode=data.copy()
    expire=datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp":expire})
    encode_jwt=jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)
    return encode_jwt

async def get_current_user(token: str = Depends(oauth2_scheme)):
  return verify_access_token(token)

def verify_access_token(token:str):
    payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    return payload
