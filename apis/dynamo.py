import json
import boto3
from boto3.dynamodb.conditions import Key
from datetime import datetime
from decimal import Decimal
from helpers import TIMESTAMP_FORMAT


class DynamoApi:
    def __init__(self):
        self.client = boto3.client('dynamodb')
        self.dynamodb = boto3.resource('dynamodb')

    def get_name(self):
        data = self._query_table('Name', 'Id', 1)
        if not data['Items']:
            return None

        return data['Items'][0]['name']

    def get_steps(self, steps_id):
        data = self._query_table('Steps', 'Id', steps_id)
        if not data['Items']:
            return None

        return data['Items'][0]

    def get_stats(self, stats_id):
        data = self._query_table('Stats', 'Id', stats_id)
        if not data['Items']:
            return None

        return data['Items'][0]

    def get_heart_rate(self, heart_rate_id):
        data = self._query_table('HeartRate', 'Id', heart_rate_id)
        if not data['Items']:
            return None

        return data['Items'][0]

    def get_activities(self, activity_id):
        data = self._query_table('Activity', 'Id', activity_id, reverse=True)
        if not data['Items']:
            return None

        return data['Items'][0]

    def get_activity_splits(self, activity_id):
        data = self._query_table('ActivitySplits', 'Id', activity_id)
        if not data['Items']:
            return None

        return data['Items'][0]['activity']

    def get_activity_details(self, activity_id):
        data = self._query_table('ActivityDetails', 'Id', activity_id)
        if not data['Items']:
            return None

        return data['Items'][0]['activity']

    def get_activity_weather(self, activity_id):
        data = self._query_table('ActivityWeather', 'Id', activity_id)
        if not data['Items']:
            return None

        return data['Items'][0]['activity']

    def get_activity_hr_zones(self, activity_id):
        data = self._query_table('ActivityHeartRateZones', 'Id', activity_id)
        if not data['Items']:
            return None

        return data['Items'][0]['activity']

    def get_device_last_used(self, device_id):
        data = self._query_table('DeviceLastUsed', 'Id', device_id)
        if not data['Items']:
            return None

        return data['Items'][0]

    def update_name(self, name):
        return self._update_table('Name', {
            'Id': 1,
            'name': name
        })

    def update_steps(self, steps_id, steps):
        ddb_steps = json.loads(json.dumps(steps), parse_float=Decimal)
        return self._update_table('Steps', {
            'Id': steps_id,
            'steps': ddb_steps,
            'timestamp': self._get_timestamp()
        })

    def update_stats(self, stats_id, stats):
        ddb_stats = json.loads(json.dumps(stats), parse_float=Decimal)
        return self._update_table('Stats', {
            'Id': stats_id,
            'stats': ddb_stats,
            'timestamp': self._get_timestamp()
        })

    def update_heart_rate(self, heart_rate_id, heart):
        ddb_heart = json.loads(json.dumps(heart), parse_float=Decimal)
        return self._update_table('HeartRate', {
            'Id': heart_rate_id,
            'heart': ddb_heart,
            'timestamp': self._get_timestamp()
        })

    def update_activities(self, activity_id, activity):
        ddb_activity = json.loads(json.dumps(activity), parse_float=Decimal)
        return self._update_table('Activity', {
            'Id': activity_id,
            'activity': ddb_activity,
            'timestamp': self._get_timestamp()
        })

    def update_activity_splits(self, activity_id, splits):
        ddb_activity = json.loads(json.dumps(splits), parse_float=Decimal)
        return self._update_table('ActivitySplits', {
            'Id': activity_id,
            'activity': ddb_activity
        })

    def update_activity_details(self, activity_id, details):
        ddb_activity = json.loads(json.dumps(details), parse_float=Decimal)
        return self._update_table('ActivityDetails', {
            'Id': activity_id,
            'activity': ddb_activity
        })

    def update_activity_weather(self, activity_id, weather):
        ddb_activity = json.loads(json.dumps(weather), parse_float=Decimal)
        return self._update_table('ActivityWeather', {
            'Id': activity_id,
            'activity': ddb_activity
        })

    def update_activity_hr_zones(self, activity_id, hr_zones):
        ddb_activity = json.loads(json.dumps(hr_zones), parse_float=Decimal)
        return self._update_table('ActivityHeartRateZones', {
            'Id': activity_id,
            'activity': ddb_activity
        })

    def update_device_last_used(self, device_id, device):
        ddb_device = json.loads(json.dumps(device), parse_float=Decimal)
        return self._update_table('DeviceLastUsed', {
            'Id': device_id,
            'device': ddb_device,
            'timestamp': self._get_timestamp()
        })

    # Helper methods

    def _query_table(self, table_name, key_name, key_val, reverse=False):
        table = self.dynamodb.Table(table_name)
        return table.query(
            KeyConditionExpression=Key(key_name).eq(key_val),
            ScanIndexForward=(not reverse)
        )

    def _update_table(self, table_name, data):
        table = self.dynamodb.Table(table_name)
        return table.put_item(Item=data)

    def _get_timestamp(self):
        return datetime.now().strftime(TIMESTAMP_FORMAT)
