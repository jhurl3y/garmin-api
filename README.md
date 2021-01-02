FastAPI wrapper around [garminconnect](https://github.com/cyberjunky/python-garminconnect), utilising [DynamoDB](https://aws.amazon.com/dynamodb/) to bypass request throttling from garmin connect.

### Run locally

1. Create `.env` file in project root like so:

```
SECRET_NAME=secret_example
SECRET_ARN=secret_example-arn
REGION=eu-west-1
STAGE=dev
NAME_TABLE=Name
ACTIVITY_TABLE=Activity
STATS_TABLE=Stats
HEART_TABLE=HeartRate
STEPS_TABLE=Steps
```

2. From terminal

```
# Set up virtualenv
pyenv virtualenv VERSION garmin-api
pyenv local garmin-api

# Install deps
pip install -r requirements.txt

# Set up aws keys
aws configure

# Start server
uvicorn main:app --reload
```
