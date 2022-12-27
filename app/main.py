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
    account_type: str
    last_name: str
    first_name: str
    age: int
    meses_uso: int
    horas_uso_dia: int 
    ayudas: str
    ocupacion: str
    PEQA: int
    PEQB: int
    PEQC: int
    PEQD: int
    PEQE: int
    PEQF: int
    PEQG: int
    PEQH: int
    PEQI: int
    PEQJ: int
    PEQK: int
    PEQL: int
    PEQM: int
    H1: str
    H2: str
    H3: str
    H4A: str
    H4A: str
    H4B: str
    H4C: str
    P1: str
    P2: str
    P3: str
    P4: str
    P5: str


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
                'meses_uso': user.meses_uso,
                'horas_uso_dia': user.horas_uso_dia,
                'ayudas': user.ayudas,
                'ocupacion': user.ocupacion,
                'PEQA': user.PEQA,
                'PEQB': user.PEQB,
                'PEQC': user.PEQC,
                'PEQD': user.PEQD,
                'PEQE': user.PEQE,
                'PEQF': user.PEQF,
                'PEQG': user.PEQG,
                'PEQH': user.PEQH,
                'PEQI': user.PEQI,
                'PEQJ': user.PEQJ,
                'PEQK': user.PEQK,
                'PEQL': user.PEQL,
                'PEQM': user.PEQM,
                'H1': user.H1,
                'H2': user.H2,
                'H3': user.H3,
                'H4A': user.H4A,
                'H4B': user.H4B,
                'H4C': user.H4C,
                'P1': user.P1,
                'P2': user.P2,
                'P3': user.P3,
                'P4': user.P4,
                'P5': user.P5

            }
        )
    return res


#test
handler = Mangum(app)