from datetime import date, timedelta, datetime

TIMESTAMP_FORMAT = '%Y-%m-%d %H:%M:%S'


def generate_id(date):
    return int(f'{date.year}{date.month}{date.day}')


def stale_data(timestamp):
    date_created = datetime.strptime(timestamp, TIMESTAMP_FORMAT)
    now = datetime.now()
    difference_in_mins = (now - date_created).total_seconds() / 60

    # Data is stale if it's greater than 60 mins old
    return difference_in_mins > 60
