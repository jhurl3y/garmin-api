import json
import boto3
from boto3.dynamodb.conditions import Key
from decimal import Decimal


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

        return data['Items'][0]['steps']

    def get_stats(self, stats_id):
        data = self._query_table('Stats', 'Id', stats_id)
        if not data['Items']:
            return None

        return data['Items'][0]['stats']

    def get_heart_rate(self, heart_rate_id):
        data = self._query_table('HeartRate', 'Id', heart_rate_id)
        if not data['Items']:
            return None

        return data['Items'][0]['heart']

    def get_activities(self, activity_id):
        data = self._query_table('Activity', 'Id', activity_id, reverse=True)
        if not data['Items']:
            return None

        return data['Items']

    def update_name(self, name):
        return self._update_table('Name', {
            'Id': 1,
            'name': name
        })

    def update_steps(self, steps_id, steps):
        ddb_steps = json.loads(json.dumps(steps), parse_float=Decimal)
        return self._update_table('Steps', {
            'Id': steps_id,
            'steps': ddb_steps
        })

    def update_stats(self, stats_id, stats):
        ddb_stats = json.loads(json.dumps(stats), parse_float=Decimal)
        return self._update_table('Stats', {
            'Id': stats_id,
            'stats': ddb_stats
        })

    def update_heart_rate(self, heart_rate_id, heart):
        ddb_heart = json.loads(json.dumps(heart), parse_float=Decimal)
        return self._update_table('HeartRate', {
            'Id': heart_rate_id,
            'heart': ddb_heart
        })

    def update_activities(self, activity_id, activity):
        ddb_activity = json.loads(json.dumps(activity), parse_float=Decimal)
        return self._update_table('Activity', {
            'Id': activity_id,
            'activity': ddb_activity
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
