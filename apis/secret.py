import boto3
import json
from botocore.exceptions import ClientError


class SecretApi:
    def __init__(self, secret_name, region):
        session = boto3.session.Session()
        self.client = session.client(
            service_name='secretsmanager',
            region_name=region
        )
        self.secret_name = secret_name

    def get_credentials(self):
        try:
            credentials = self.client.get_secret_value(
                SecretId=self.secret_name
            )
        except ClientError as e:
            return

        return json.loads(credentials['SecretString'])
