import sys
import os
# sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)) + os.sep + 'data_manage')
# # sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# print(sys.path)
# print(os.getcwd())
# sys.path.append('.')
# print(sys.path)

from django.shortcuts import render
from django.http import JsonResponse

from ..data_manage.series_query import get_recent_record


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
