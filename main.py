import os
from fastapi import FastAPI, HTTPException
from GarminApi import GarminApi
from datetime import date, timedelta
from dotenv import load_dotenv
from typing import List
from models import (Root, Name, Step, Stats, HeartRate)

# Load email and password
load_dotenv()
EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")

app = FastAPI()
api = GarminApi(email=EMAIL, password=PASSWORD)


@app.get('/', response_model=Root)
async def root():
    return {'message': 'Hello James'}

@app.get('/name', response_model=Name)
async def name():
    if not api:
        raise HTTPException(status_code=400, detail='Error logging in')

    data = api.get_name()

    if not data:
        raise HTTPException(status_code=400, detail='Error logging in')

    if 'error' in data:
        raise HTTPException(status_code=500, detail=data.get('message'))

    return {'name': data}

@app.get('/steps', response_model=List[Step])
async def steps():
    if not api:
        raise HTTPException(status_code=400, detail='Error logging in')

    yesterday = date.today() - timedelta(1)
    data = api.get_steps(yesterday.isoformat())

    if not data:
        raise HTTPException(status_code=400, detail='Error logging in')

    if 'error' in data:
        raise HTTPException(status_code=500, detail=data.get('message'))

    return data

@app.get('/stats', response_model=Stats)
async def stats():
    if not api:
        raise HTTPException(status_code=400, detail='Error logging in')

    yesterday = date.today() - timedelta(1)
    data = api.get_stats(yesterday.isoformat())

    if not data:
        raise HTTPException(status_code=400, detail='Error logging in')

    if 'error' in data:
        raise HTTPException(status_code=500, detail=data.get('message'))

    return data

@app.get('/heart_rate', response_model=HeartRate)
async def heart_rate():
    if not api:
        raise HTTPException(status_code=400, detail='Error logging in')

    yesterday = date.today() - timedelta(1)
    data = api.get_heart_rate(yesterday.isoformat())

    if not data:
        raise HTTPException(status_code=400, detail='Error logging in')

    if 'error' in data:
        raise HTTPException(status_code=500, detail=data.get('message'))

    return data