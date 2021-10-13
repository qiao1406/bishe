from .models import Record


def query(start_date, end_date, sensors):
    if not sensors:
        raise ValueError('Empty sensors')
    series = []
    for sensor in sensors:
        q = Record.objects.filter(time__range=(start_date, end_date), sensor=sensor).order_by('time').values('val')
        series.append({'name': sensor, 'type': 'line', 'data': [r['val'] for r in q]})

    return series


if __name__ == '__main__':
    query('2020-01-01', '2020-02-01')