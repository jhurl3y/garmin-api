FastAPI wrapper around [garminconnect](https://github.com/cyberjunky/python-garminconnect), utilising [DynamoDB](https://aws.amazon.com/dynamodb/) to bypass request throttling from garmin connect.

### Run locally

1. Create `.env` file in project root like so:

```
EMAIL = 'email@gmail.com' # garmin email
PASSWORD = 'passpass' # garmin password
AWS_DEFAULT_REGION=eu-west-1
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
