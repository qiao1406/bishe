import datetime
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from .series_query import query


def show(request):
    return render(request, 'data_show.html')


def show_trend(request):
    def parse_date(s):
        s1, s2 = s.split('T')
        i = s2.find(':')
        return s1 + ' ' + s2[:i + 1] + '00:00'

    def gen_date_range(sd, ed):
        fmt = '%Y-%m-%d %H:%M:%S'
        sd_obj, ed_obj = datetime.datetime.strptime(sd, fmt), datetime.datetime.strptime(ed, fmt)
        date_range = []
        d = sd_obj
        while d <= ed_obj:
            date_range.append(d.strftime(fmt))
            d += datetime.timedelta(hours=1)
        return date_range

    qd = request.GET
    sensors = qd['selected_sensors'].split(',')
    start_date = parse_date(qd['start_date'])
    end_date = parse_date(qd['end_date'])

    ret = dict()
    ret['legend'] = [{'name': sensor, 'icon': 'circle'} for sensor in sensors]
    ret['series'] = query(start_date, end_date, sensors)
    ret['xAxis'] = gen_date_range(start_date, end_date)
    return JsonResponse(ret)