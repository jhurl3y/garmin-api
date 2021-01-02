class Error(Exception):
    """Base class for other exceptions"""
    pass


class SecretsError(Error):
    """Raised for aws secrets manager errors"""
    pass


class GarminLoginError(Error):
    """Raised for garmin api login errors"""
    pass
