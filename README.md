FastAPI wrapper around [garminconnect](https://github.com/cyberjunky/python-garminconnect), utilising [DynamoDB](https://aws.amazon.com/dynamodb/) to bypass request throttling from garmin connect, hosted on [AWS](https://aws.amazon.com).

### To run yourself

1. Create the following [DynamoDB](https://aws.amazon.com/dynamodb/) tables, with `Id` as the partition key:

```
Name
Activity
Stats
HeartRate
Steps
```

2. Add your garmin email/password to [Secrets Manager](https://aws.amazon.com/secrets-manager/). Call it something e.g. `secret_example` and add two rows, `EMAIL` and `PASSWORD` with your actual garmin email/password.

3. Create `.env` file in project root like so:

```
SECRET_NAME=secret_example
SECRET_ARN=secret_example-arn # arn for secret created
REGION=eu-west-1
STAGE=dev
NAME_TABLE=Name
ACTIVITY_TABLE=Activity
STATS_TABLE=Stats
HEART_TABLE=HeartRate
STEPS_TABLE=Steps
```

4. From the terminal:

```
# Set up virtualenv
pyenv virtualenv VERSION garmin-api
pyenv local garmin-api

# Install deps
pip install -r requirements.txt
npm i -g serverless
npm i

# Set up aws keys
aws configure

# Start server locally
uvicorn main:app --reload

# Test serverless offline
sls offline

# Deploy to aws
npm run deploy-dev
npm run deploy-prod
```
