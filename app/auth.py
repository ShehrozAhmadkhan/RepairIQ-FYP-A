from passlib.context import CryptContext
from jose import JWTError, jwt
from datetime import datetime, timedelta
import os

SECRET_KEY = "RepairIQ-fypA-2026"
ALGORITHM = "HS256"
ACCESS_TOKEN_LIMIT = 60

pwd_context = CryptContext(schemes=["bcrypt"], deprecated = "auto")

#pwd_context.hash() to create ahash password
#pwd_context.verify() to check wether the password and hash created password are same

def hash_password(password:str):
    return pwd_context.hash(password)

def verify_password(plain_password:str,hashed_password:str):
    return pwd_context.verify(plain_password,hashed_password)

#def create_jwt():

def create_token(data:dict):
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_LIMIT)
    data.update({"exp" : expire})

    return jwt.encode(data,SECRET_KEY,algorithm = ALGORITHM)