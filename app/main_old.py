import sys
import os
import time
import boto3
sys.path.append(".")
from fastapi import FastAPI
from pydantic import BaseModel
from mangum import Mangum

class NewUser(BaseModel):
    registro: str
    usuario: str
    first_name: str
    last_name: str
    age: int
    account_type: str

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Healthcheck"}


@app.post("/newuser/")#, response_model=BenchmarkIn)
async def create_in(user: NewUser):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('mahavir-app')
    registro= str(int(time.time()))+user.usuario
    res = table.put_item(
        Item={
                'registro': registro,
                'usuario': user.usuario,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'age': user.age,
                'account_type': user.account_type,
            }
        )
    return res


#test
handler = Mangum(app)