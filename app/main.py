from fastapi import FastAPI, File, UploadFile
from database import add_user, add_chat, add_manuals, get_user
from auth import hash_password, verify_password, create_token
from pydantic import BaseModel 

app = FastAPI()

class SignupRequest(BaseModel):
    email : str
    password : str

class LoginRequest(BaseModel):
    email : str
    password : str


@app.post("/signup")

def signup(data : SignupRequest):
    email = data.email
    password = data.password
    h_p = hash_password(password)
    add_user(email,h_p)

    return {"Request" : "success"}

@app.post("/login")

def login(data : LoginRequest):
    email = data.email
    password = data.password
    record = get_user(email)
    if not record:
        return {"message" : "email not found."}

    if not verify_password(password,record.password):
        return {"message" : "incorrect password."}
    data = {"email": email}
    jwt = create_token(data)

    return {"jwt" : jwt}



@app.post("/upload")

async def upload(file: UploadFile = File(...)):
    data = await file.read()
    temp = open("temp.pdf","wb")
    temp.write(data)
    temp.close()
    add_manuals(1,"temp.pdf")
    return {"message" : "success"}
