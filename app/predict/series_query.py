from .models import Record


def query(start_date, end_date, sensors):
    if not sensors:
        raise ValueError('Empty sensors')
    series = []
    for sensor in sensors:
        q = Record.objects.filter(time__range=(start_date, end_date), sensor=sensor).order_by('time').values('val')
        series.append({'name': sensor, 'type': 'line', 'data': [r['val'] for r in q]})

    return series


def get_recent_record(sensors, num):
    if not sensors:
        raise ValueError('Empty sensors')
    series = []
    for sensor in sensors:
        q = Record.objects.filter(sensor=sensor).order_by('-time').values('val')[:num]
        data = [r['val'] for r in reversed(list(q))]
        series.append({'name': sensor, 'type': 'line', 'data': data})

    q = Record.objects.values('time').distinct().order_by('-time')[:num]
    time_records = [r['time'].strftime('%Y-%m-%d %H:%M:%S') for r in reversed(list(q))]
    return series, time_records
