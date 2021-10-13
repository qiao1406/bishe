from django.urls import path

from . import views

urlpatterns = [
    path('show/', views.show, name='show'),
    path('show/get_model_detail/', views.get_model_detail, name='get_model_detail')
]
