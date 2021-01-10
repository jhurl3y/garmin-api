from botocore.exceptions import ClientError
import base64
import boto3
import os
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
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


# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# apis
dynamo = DynamoApi()
secret = SecretApi(secret_name=SECRET_NAME, region=REGION)
garmin = GarminApi(secret_api=secret)


@app.get('/', response_model=Root)
async def root():
    return {'message': 'Hello James'}


@app.get('/name', response_model=Name)
async def name():
    db_data = dynamo.get_name()

    # Successfully loaded from db
    if db_data:
        return {'name': dadb_datata}

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
    db_data = dynamo.get_steps(steps_id)

    # Successfully loaded from db
    if db_data:
        return db_data

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
    db_data = dynamo.get_stats(stats_id)

    # Successfully loaded from db
    if db_data:
        return db_data

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
    db_data = dynamo.get_heart_rate(heart_rate_id)

    # Successfully loaded from db
    if db_data:
        return db_data

    data = garmin.get_heart_rate(yesterday.isoformat())

    if 'error' in data:
        raise HTTPException(status_code=500, detail=data.get('msg'))

    # Update in db
    dynamo.update_heart_rate(heart_rate_id, data)

    return data


@app.get('/last_activity', response_model=Activity)
async def last_activity():
    return _get_last_activity()


@app.get('/last_activity_splits')
async def last_activity_splits():
    activity = _get_last_activity()
    activity_id = int(activity['activityId'])
    db_data = dynamo.get_activity_splits(activity_id)

    # Successfully loaded from db
    if db_data:
        return db_data

    data = garmin.get_activity_splits(activity_id)

    if 'error' in data:
        raise HTTPException(status_code=500, detail=data.get('msg'))

    # Update in db
    dynamo.update_activity_splits(activity_id, data)

    return data


@app.get('/last_activity_details')
async def last_activity_details():
    activity = _get_last_activity()
    activity_id = int(activity['activityId'])
    db_data = dynamo.get_activity_details(activity_id)

    # Successfully loaded from db
    if db_data:
        return db_data

    data = garmin.get_activity_details(activity_id)

    if 'error' in data:
        raise HTTPException(status_code=500, detail=data.get('msg'))

    # Update in db
    dynamo.update_activity_details(activity_id, data)

    return data


@app.get('/last_activity_weather')
async def last_activity_weather():
    activity = _get_last_activity()
    activity_id = int(activity['activityId'])
    db_data = dynamo.get_activity_weather(activity_id)

    # Successfully loaded from db
    if db_data:
        return db_data

    data = garmin.get_activity_weather(activity_id)

    if 'error' in data:
        raise HTTPException(status_code=500, detail=data.get('msg'))

    # Update in db
    dynamo.update_activity_weather(activity_id, data)

    return data


@app.get('/last_activity_hr_zones')
async def last_activity_hr_zones():
    activity = _get_last_activity()
    activity_id = int(activity['activityId'])
    db_data = dynamo.get_activity_hr_zones(activity_id)

    # Successfully loaded from db
    if db_data:
        return db_data

    data = garmin.get_activity_hr_zones(activity_id)

    if 'error' in data:
        raise HTTPException(status_code=500, detail=data.get('msg'))

    # Update in db
    dynamo.update_activity_hr_zones(activity_id, data)

    return data


@app.get('/last_device_used')
async def last_device_used():
    yesterday = (date.today() - timedelta(1))
    device_id = generate_id(yesterday)
    db_data = dynamo.get_device_last_used(device_id)

    # Successfully loaded from db
    if db_data:
        return db_data

    data = garmin.get_device_last_used()

    if 'error' in data:
        raise HTTPException(status_code=500, detail=data.get('msg'))

    # Update in db
    dynamo.update_device_last_used(device_id, data)

    return data


def _get_last_activity():
    activity_id = generate_id(date.today())
    db_data = dynamo.get_activities(activity_id)

    # Successfully loaded from db
    if db_data:
        return db_data['activity']

    data = garmin.get_activities(limit=1)

    if 'error' in data:
        raise HTTPException(status_code=500, detail=data.get('msg'))

    activity = data[0]

    # Update in db
    dynamo.update_activities(activity_id, activity)

    return activity


handler = Mangum(app)
