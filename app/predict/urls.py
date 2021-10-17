from django.urls import path

from . import views

urlpatterns = [
    path('load_last50/', views.load_last50_record, name='load_last50'),
    path('', views.predict_index, name='predict_index')
]
