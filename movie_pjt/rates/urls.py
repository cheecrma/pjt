from django.urls import path
from . import views

app_name = 'rates'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:movie_pk>/', views.detail, name='detail'),
    path('<int:movie_pk>/rate/',views.rate_create, name='rate_create'),
    path('<int:movie_pk>/rate/<int:rate_pk>/delete/', views.rate_delete, name='rate_delete'),
]
