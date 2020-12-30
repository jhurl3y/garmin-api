from datetime import date, timedelta


def generate_id():
    yesterday = (date.today())
    return int(f'{yesterday.year}{yesterday.month}{yesterday.day}')
