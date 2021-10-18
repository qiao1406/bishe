from django.urls import path

from . import views

urlpatterns = [
    path('predict/', views.predict_index, name='predict_index'),
    path('predict/load_last50/', views.load_last50_record, name='load_last50'),
    path('predict/detect_model/', views.detect_model, name='detect_model'),
    path('data_manage/show/', views.data_show, name='data_show'),
    path('data_manage/show_trend/', views.show_trend, name='trend_detail'),
    path('model_manage/show/', views.model_show, name='model_show'),
    path('model_manage/show/get_model_detail/', views.get_model_detail, name='get_model_detail')
]
