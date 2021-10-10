from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return HttpResponse("Data Manage")


def show(request):
    # return HttpResponse('fuckyou')
    return render(request, 'data_show.html')
