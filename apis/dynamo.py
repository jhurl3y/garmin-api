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

    def get_steps(self, date):
        data = self._query_table('Steps', 'date', date)
        if not data['Items']:
            return None

        return data['Items'][0]['steps']

    def get_stats(self, date):
        data = self._query_table('Stats', 'date', date)
        if not data['Items']:
            return None

        return data['Items'][0]['stats']

    def get_heart_rate(self, date):
        data = self._query_table('HeartRate', 'date', date)
        if not data['Items']:
            return None

        return data['Items'][0]['heart']

    def update_name(self, name):
        return self._update_table('Name', {
            'Id': 1,
            'name': name
        })

    def update_steps(self, date, steps):
        ddb_steps = json.loads(json.dumps(steps), parse_float=Decimal)
        return self._update_table('Steps', {
            'date': date,
            'steps': ddb_steps
        })

    def update_stats(self, date, stats):
        ddb_stats = json.loads(json.dumps(stats), parse_float=Decimal)
        return self._update_table('Stats', {
            'date': date,
            'stats': ddb_stats
        })

    def update_heart_rate(self, date, heart):
        ddb_heart = json.loads(json.dumps(heart), parse_float=Decimal)
        return self._update_table('HeartRate', {
            'date': date,
            'heart': ddb_heart
        })

    # Helper methods

    def _query_table(self, table_name, key_name, key_val):
        table = self.dynamodb.Table(table_name)
        return table.query(
            KeyConditionExpression=Key(key_name).eq(key_val)
        )

    def _update_table(self, table_name, data):
        table = self.dynamodb.Table(table_name)
        return table.put_item(Item=data)
