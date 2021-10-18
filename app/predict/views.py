from django.shortcuts import render
from django.http import JsonResponse, HttpResponse

from .series_query import get_recent_record, query
from .models import ModelRecord
from .utils import *


def data_show(request):
    return render(request, 'data_show.html')


def show_trend(request):
    qd = request.GET
    sensors = qd['selected_sensors'].split(',')
    start_date = parse_date(qd['start_date'])
    end_date = parse_date(qd['end_date'])

    ret = dict()
    ret['legend'] = [{'name': sensor, 'icon': 'circle'} for sensor in sensors]
    ret['series'] = query(start_date, end_date, sensors)
    ret['xAxis'] = gen_date_range(start_date, end_date)
    return JsonResponse(ret)


def model_show(request):
    return render(request, 'model_show.html')


def get_model_detail(request):
    q = ModelRecord.objects.all().values()
    return JsonResponse({'data': list(q)})


def predict_index(request):
    return render(request, 'predict.html')


def load_last50_record(request):
    sensors = request.GET['selected_sensors'].split(',')
    ret = dict()
    ret['legend'] = [{'name': sensor, 'icon': 'circle'} for sensor in sensors]
    series, x_axis = get_recent_record(sensors, 50)
    ret['series'] = series
    ret['xAxis'] = x_axis
    return JsonResponse(ret)


def detect_model(request):
    print('detect')
    r = request.GET
    q = ModelRecord.objects.filter(model_name=r['model_name'],
                                   observe_window=r['observe_window'],
                                   predict_gap=r['predict_gap'],
                                   predict_len=r['predict_length'],
                                   para_d=r['para_d'],
                                   para_r=r['para_r']
                                   )

    if q:
        return HttpResponse('yes', status=200)
    else:
        return HttpResponse('none', status=404)
