from datetime import date, timedelta


def generate_id(date):
    return int(f'{date.year}{date.month}{date.day}')
