from garminconnect import (
    Garmin,
    GarminConnectConnectionError,
    GarminConnectTooManyRequestsError,
    GarminConnectAuthenticationError,
)
from exceptions import SecretsError, GarminLoginError


class GarminApi:
    def __init__(self, secret_api):
        self.secret_api = secret_api
        self.client = None

    def get_steps(self, date):
        # Log in to garmin
        if not self.client:
            try:
                self.client = self._get_client()
            except (SecretsError, GarminLoginError) as e:
                return {
                    'error': True,
                    'msg': f'Login error: {str(e)}'
                }

        # Fetch steps
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
        # Log in to garmin
        if not self.client:
            try:
                self.client = self._get_client()
            except (SecretsError, GarminLoginError) as e:
                return {
                    'error': True,
                    'msg': f'Login error: {str(e)}'
                }

        # Fetch name
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
        # Log in to garmin
        if not self.client:
            try:
                self.client = self._get_client()
            except (SecretsError, GarminLoginError) as e:
                return {
                    'error': True,
                    'msg': f'Login error: {str(e)}'
                }

        # Fetch stats
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
        # Log in to garmin
        if not self.client:
            try:
                self.client = self._get_client()
            except (SecretsError, GarminLoginError) as e:
                return {
                    'error': True,
                    'msg': f'Login error: {str(e)}'
                }

        # Fetch heart rates
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

    def get_activities(self, limit):
        # Log in to garmin
        if not self.client:
            try:
                self.client = self._get_client()
            except (SecretsError, GarminLoginError) as e:
                return {
                    'error': True,
                    'msg': f'Login error: {str(e)}'
                }

        # Fetch activities
        try:
            return self.client.get_activities(0, limit)
        except (
            GarminConnectConnectionError,
            GarminConnectAuthenticationError,
            GarminConnectTooManyRequestsError
        ) as e:
            return {
                'error': True,
                'msg': f'GarminConnect error: {e.status}'
            }

    def get_activity_splits(self, activity_id):
        # Log in to garmin
        if not self.client:
            try:
                self.client = self._get_client()
            except (SecretsError, GarminLoginError) as e:
                return {
                    'error': True,
                    'msg': f'Login error: {str(e)}'
                }

        # Fetch splits
        try:
            return self.client.get_activity_splits(activity_id)
        except (
            GarminConnectConnectionError,
            GarminConnectAuthenticationError,
            GarminConnectTooManyRequestsError
        ) as e:
            return {
                'error': True,
                'msg': f'GarminConnect error: {e.status}'
            }

    def get_activity_details(self, activity_id):
        # Log in to garmin
        if not self.client:
            try:
                self.client = self._get_client()
            except (SecretsError, GarminLoginError) as e:
                return {
                    'error': True,
                    'msg': f'Login error: {str(e)}'
                }

        # Fetch details
        try:
            return self.client.get_activity_details(activity_id)
        except (
            GarminConnectConnectionError,
            GarminConnectAuthenticationError,
            GarminConnectTooManyRequestsError
        ) as e:
            return {
                'error': True,
                'msg': f'GarminConnect error: {e.status}'
            }

    def get_activity_weather(self, activity_id):
        # Log in to garmin
        if not self.client:
            try:
                self.client = self._get_client()
            except (SecretsError, GarminLoginError) as e:
                return {
                    'error': True,
                    'msg': f'Login error: {str(e)}'
                }

        # Fetch weather
        try:
            return self.client.get_activity_weather(activity_id)
        except (
            GarminConnectConnectionError,
            GarminConnectAuthenticationError,
            GarminConnectTooManyRequestsError
        ) as e:
            return {
                'error': True,
                'msg': f'GarminConnect error: {e.status}'
            }

    def get_activity_hr_zones(self, activity_id):
        # Log in to garmin
        if not self.client:
            try:
                self.client = self._get_client()
            except (SecretsError, GarminLoginError) as e:
                return {
                    'error': True,
                    'msg': f'Login error: {str(e)}'
                }

        # Fetch hr zones
        try:
            return self.client.get_activity_hr_in_timezones(activity_id)
        except (
            GarminConnectConnectionError,
            GarminConnectAuthenticationError,
            GarminConnectTooManyRequestsError
        ) as e:
            return {
                'error': True,
                'msg': f'GarminConnect error: {e.status}'
            }

    def get_device_last_used(self):
        # Log in to garmin
        if not self.client:
            try:
                self.client = self._get_client()
            except (SecretsError, GarminLoginError) as e:
                return {
                    'error': True,
                    'msg': f'Login error: {str(e)}'
                }

        # Fetch device
        try:
            return self.client.get_device_last_used()
        except (
            GarminConnectConnectionError,
            GarminConnectAuthenticationError,
            GarminConnectTooManyRequestsError
        ) as e:
            return {
                'error': True,
                'msg': f'GarminConnect error: {e.status}'
            }

    def _get_client(self):
        credentials = self.secret_api.get_credentials()
        if not credentials:
            raise SecretsError('Error fetching garmin login credentials')
        try:
            client = Garmin(credentials["EMAIL"], credentials["PASSWORD"])
            client.login()
            return client
        except (
            GarminConnectConnectionError,
            GarminConnectAuthenticationError,
            GarminConnectTooManyRequestsError
        ):
            raise GarminLoginError('Error logging into garmin')
