# import function CryptContext to perform the action of has and unhash
from passlib.context import CryptContext

pwd_cxt = CryptContext(schemes=["bcrypt"],deprecated="auto")

class Hash:
    def hash_password(password:str):
        return pwd_cxt.hash(password)
    def verify_password(password:str, hashed_password:str):
        return pwd_cxt.verify(password, hashed_password)