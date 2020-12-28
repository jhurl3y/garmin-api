from garminconnect import (
    Garmin,
    GarminConnectConnectionError,
    GarminConnectTooManyRequestsError,
    GarminConnectAuthenticationError,
)

class GarminApi:
    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.client = self.get_client()

    def get_client(self):
        try:
            client = Garmin(self.email, self.password)
            client.login()
            return client
        except (
            GarminConnectConnectionError,
            GarminConnectAuthenticationError,
            GarminConnectTooManyRequestsError
        ):
            return None

    def get_steps(self, date):
        if not self.client:
            return None
        
        try:
            return self.client.get_steps_data(date)
        except (
            GarminConnectConnectionError,
            GarminConnectAuthenticationError,
            GarminConnectTooManyRequestsError
        ) as e:
            return {
                'error': True,
                'msg': f'GarminConnect error: {e.status}'
            }

    def get_name(self):
        if not self.client:
            return None
        
        try:
            return self.client.get_full_name()
        except (
            GarminConnectConnectionError,
            GarminConnectAuthenticationError,
            GarminConnectTooManyRequestsError
        ) as e:
            return {
                'error': True,
                'msg': f'GarminConnect error: {e.status}'
            }

    def get_stats(self, date):
        if not self.client:
            return None
        
        try:
            return self.client.get_stats(date)
        except (
            GarminConnectConnectionError,
            GarminConnectAuthenticationError,
            GarminConnectTooManyRequestsError
        ) as e:
            return {
                'error': True,
                'msg': f'GarminConnect error: {e.status}'
            }

    def get_heart_rate(self, date):
        if not self.client:
            return None
        
        try:
            return self.client.get_heart_rates(date)
        except (
            GarminConnectConnectionError,
            GarminConnectAuthenticationError,
            GarminConnectTooManyRequestsError
        ) as e:
            return {
                'error': True,
                'msg': f'GarminConnect error: {e.status}'
            }