from django.urls import path
from . import views

app_name = "movies"
urlpatterns = [
    path('', views.index, name='index'),
    path('result_on/', views.result_on, name='result_on'),
    path('result_off/', views.result_off, name='result_off'),
]
