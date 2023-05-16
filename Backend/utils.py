# import function CryptContext to perform the action of has and unhash
from passlib.context import CryptContext

pwd_cxt = CryptContext(schemes=["bcrypt"],deprecated="auto")

# contains function of hashing and de-hashing the password
class Hash:
    def hash_password(pwd:str):
        return pwd_cxt.hash(pwd)
    def verify_password(pwd:str, hashed_password:str):
        return pwd_cxt.verify(pwd, hashed_password)