from django.shortcuts import render


def predict_index(request):
    return render(request, 'predict.html')

