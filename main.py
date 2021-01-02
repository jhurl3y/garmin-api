from botocore.exceptions import ClientError
import base64
import boto3
import os
from fastapi import FastAPI, HTTPException
from mangum import Mangum
from apis.dynamo import DynamoApi
from apis.garmin import GarminApi
from apis.secret import SecretApi
from datetime import date, timedelta
from dotenv import load_dotenv
from helpers import generate_id
from typing import List
from models import (Root, Name, Step, Stats, HeartRate, Activity)

# Load email and password
load_dotenv()
SECRET_NAME = os.getenv("SECRET_NAME")
REGION = os.getenv("REGION")

app = FastAPI()

# apis
dynamo = DynamoApi()
secret = SecretApi(secret_name=SECRET_NAME, region=REGION)
garmin = GarminApi(secret_api=secret)


@app.get('/', response_model=Root)
async def root():
    return {'message': 'Hello James'}


@app.get('/name', response_model=Name)
async def name():
    data = dynamo.get_name()

    # Successfully loaded from db
    if data:
        return {'name': data}

    data = garmin.get_name()

    if 'error' in data:
        raise HTTPException(status_code=500, detail=data.get('msg'))

    # Update in db
    dynamo.update_name(data)

    return {'name': data}


@app.get('/steps', response_model=List[Step])
async def steps():
    yesterday = (date.today() - timedelta(1))
    steps_id = generate_id(yesterday)
    data = dynamo.get_steps(steps_id)

    # Successfully loaded from db
    if data:
        return data

    data = garmin.get_steps(yesterday.isoformat())

    if 'error' in data:
        raise HTTPException(status_code=500, detail=data.get('msg'))

    # Update in db
    dynamo.update_steps(steps_id, data)

    return data


@app.get('/stats', response_model=Stats)
async def stats():
    yesterday = (date.today() - timedelta(1))
    stats_id = generate_id(yesterday)
    data = dynamo.get_stats(stats_id)

    # Successfully loaded from db
    if data:
        return data

    data = garmin.get_stats(yesterday.isoformat())

    if 'error' in data:
        raise HTTPException(status_code=500, detail=data.get('msg'))

    # Update in db
    dynamo.update_stats(stats_id, data)

    return data


@app.get('/heart_rate', response_model=HeartRate)
async def heart_rate():
    yesterday = (date.today() - timedelta(1))
    heart_rate_id = generate_id(yesterday)
    data = dynamo.get_heart_rate(heart_rate_id)

    # Successfully loaded from db
    if data:
        return data

    data = garmin.get_heart_rate(yesterday.isoformat())

    if 'error' in data:
        raise HTTPException(status_code=500, detail=data.get('msg'))

    # Update in db
    dynamo.update_heart_rate(heart_rate_id, data)

    return data


@app.get('/last_activity', response_model=Activity)
async def last_activity():
    activity_id = generate_id(date.today())
    db_data = dynamo.get_activities(activity_id)

    # Successfully loaded from db
    if db_data:
        return db_data[0]['activity']

    data = garmin.get_activities(limit=1)

    if 'error' in data:
        raise HTTPException(status_code=500, detail=data.get('msg'))

    activity = data[0]

    # Update in db
    dynamo.update_activities(activity_id, activity)

    return activity

handler = Mangum(app)
