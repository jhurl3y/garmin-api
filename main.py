import logging
from botocore.exceptions import ClientError
import base64
import boto3
import os
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional
from mangum import Mangum
from apis.dynamo import DynamoApi
from apis.garmin import GarminApi
from apis.secret import SecretApi
from datetime import date, timedelta
from dotenv import load_dotenv
from helpers import generate_id, stale_data
from typing import List
from models import (Root, Name, Step, Stats, HeartRate,
                    Activity, Device, Weather, HRZone, Split, Details, FullActivity)

# Load email and password
load_dotenv()
SECRET_NAME = os.getenv("SECRET_NAME")
REGION = os.getenv("REGION")

app = FastAPI()

# Enable debug logging
logging.basicConfig(level=logging.DEBUG)


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
    if db_data and not stale_data(db_data['timestamp']):
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
    if db_data and not stale_data(db_data['timestamp']):
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
    if db_data and not stale_data(db_data['timestamp']):
        return db_data

    data = garmin.get_heart_rate(yesterday.isoformat())

    if 'error' in data:
        raise HTTPException(status_code=500, detail=data.get('msg'))

    # Update in db
    dynamo.update_heart_rate(heart_rate_id, data)

    return data


@app.get('/last_device_used', response_model=Device)
async def last_device_used():
    yesterday = (date.today() - timedelta(1))
    device_id = generate_id(yesterday)
    db_data = dynamo.get_device_last_used(device_id)

    # Successfully loaded from db
    if db_data and not stale_data(db_data['timestamp']):
        return db_data

    data = garmin.get_device_last_used()

    if 'error' in data:
        raise HTTPException(status_code=500, detail=data.get('msg'))

    # Update in db
    dynamo.update_device_last_used(device_id, data)

    return data


@app.get('/last_activity_summary', response_model=Activity)
async def last_activity_summary():
    return _get_last_activity()


@app.get('/last_activity_splits', response_model=Split)
async def last_activity_splits():
    activity = _get_last_activity()
    activity_id = int(activity['activityId'])
    return _get_splits(activity_id)


@app.get('/last_activity_details', response_model=Details)
async def last_activity_details():
    activity = _get_last_activity()
    activity_id = int(activity['activityId'])
    return _get_details(activity_id)


@app.get('/last_activity_weather', response_model=Weather)
async def last_activity_weather():
    activity = _get_last_activity()
    activity_id = int(activity['activityId'])
    return _get_weather(activity_id)


@app.get('/last_activity_hr_zones', response_model=List[HRZone])
async def last_activity_hr_zones():
    activity = _get_last_activity()
    activity_id = int(activity['activityId'])
    return _get_hr_zones(activity_id)


@app.get('/last_activity', response_model=FullActivity)
async def last_activity(
    include_splits: Optional[bool] = False,
    include_details: Optional[bool] = False,
    include_weather: Optional[bool] = False,
    include_hr_zones: Optional[bool] = False,
):
    data = {
        'summary': None,
        'splits': None,
        'details': None,
        'weather': None,
        'hr_zones': None,
    }
    activity = _get_last_activity()
    activity_id = int(activity['activityId'])

    # Build the data to return
    data['summary'] = activity

    if include_splits:
        data['splits'] = _get_splits(activity_id)

    if include_details:
        data['details'] = _get_details(activity_id)

    if include_weather:
        data['weather'] = _get_weather(activity_id)

    if include_hr_zones:
        data['hr_zones'] = _get_hr_zones(activity_id)

    return data


def _get_last_activity():
    activity_id = generate_id(date.today())
    db_data = dynamo.get_activities(activity_id)

    # Successfully loaded from db
    if db_data and not stale_data(db_data['timestamp']):
        return db_data['activity']

    data = garmin.get_activities(limit=10)

    if 'error' in data:
        raise HTTPException(status_code=500, detail=data.get('msg'))

    # Only want to return running for time being
    activity = next(
        a for a in data if a['activityType']['typeKey'] == 'running')

    # Update in db
    dynamo.update_activities(activity_id, activity)

    return activity


def _get_splits(activity_id):
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


def _get_details(activity_id):
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


def _get_weather(activity_id):
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


def _get_hr_zones(activity_id):
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


handler = Mangum(app)
