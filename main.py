import os
from fastapi import FastAPI, HTTPException
from apis.dynamo import DynamoApi
from apis.garmin import GarminApi
from datetime import date, timedelta
from dotenv import load_dotenv
from helpers import generate_id
from typing import List
from models import (Root, Name, Step, Stats, HeartRate, Activity)

# Load email and password
load_dotenv()
EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")


app = FastAPI()
dynamo = DynamoApi()
garmin = GarminApi(email=EMAIL, password=PASSWORD)


@app.get('/', response_model=Root)
async def root():
    return {'message': 'Hello James'}


@app.get('/name', response_model=Name)
async def name():
    data = dynamo.get_name()

    # Successfully loaded from db
    if data:
        return {'name': data}

    if not garmin:
        raise HTTPException(status_code=400, detail='Error logging in')

    data = garmin.get_name()

    if not data:
        raise HTTPException(status_code=400, detail='Error logging in')

    if 'error' in data:
        raise HTTPException(status_code=500, detail=data.get('message'))

    # Update in db
    dynamo.update_name(data)

    return {'name': data}


@app.get('/steps', response_model=List[Step])
async def steps():
    yesterday = (date.today() - timedelta(1)).isoformat()
    data = dynamo.get_steps(yesterday)

    # Successfully loaded from db
    if data:
        return data

    if not garmin:
        raise HTTPException(status_code=400, detail='Error logging in')

    data = garmin.get_steps(yesterday)

    if not data:
        raise HTTPException(status_code=400, detail='Error logging in')

    if 'error' in data:
        raise HTTPException(status_code=500, detail=data.get('message'))

    # Update in db
    dynamo.update_steps(yesterday, data)

    return data


@app.get('/stats', response_model=Stats)
async def stats():
    yesterday = (date.today() - timedelta(1)).isoformat()
    data = dynamo.get_stats(yesterday)

    # Successfully loaded from db
    if data:
        return data

    if not garmin:
        raise HTTPException(status_code=400, detail='Error logging in')

    data = garmin.get_stats(yesterday)

    if not data:
        raise HTTPException(status_code=400, detail='Error logging in')

    if 'error' in data:
        raise HTTPException(status_code=500, detail=data.get('message'))

    # Update in db
    dynamo.update_stats(yesterday, data)

    return data


@app.get('/heart_rate', response_model=HeartRate)
async def heart_rate():
    yesterday = (date.today() - timedelta(1)).isoformat()
    data = dynamo.get_heart_rate(yesterday)

    # Successfully loaded from db
    if data:
        return data

    if not garmin:
        raise HTTPException(status_code=400, detail='Error logging in')

    data = garmin.get_heart_rate(yesterday)

    if not data:
        raise HTTPException(status_code=400, detail='Error logging in')

    if 'error' in data:
        raise HTTPException(status_code=500, detail=data.get('message'))

    # Update in db
    dynamo.update_heart_rate(yesterday, data)

    return data


@app.get('/last_activity', response_model=Activity)
async def last_activity():
    activity_id = generate_id()
    db_data = dynamo.get_activities(activity_id)

    # Successfully loaded from db
    if db_data:
        return db_data[0]['activity']

    data = garmin.get_activities(limit=1)

    if not data:
        raise HTTPException(status_code=400, detail='Error logging in')

    if 'error' in data:
        raise HTTPException(status_code=500, detail=data.get('message'))

    activity = data[0]

    # Update in db
    dynamo.update_activities(activity_id, activity)

    return activity
