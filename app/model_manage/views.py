from django.shortcuts import render
from django.http import JsonResponse

from .models import ModelRecord


def show(request):
    return render(request, 'model_show.html')


def get_model_detail(request):
    q = ModelRecord.objects.all().values()
    return JsonResponse({'data': list(q)})
