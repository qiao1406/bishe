from django.urls import path

from . import views

urlpatterns = [
    path('show/', views.show, name='show'),
    path('show_trend/', views.show_trend, name='trend_detail'),
    path('', views.show, name='index'),
]
