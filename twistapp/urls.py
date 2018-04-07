from django.urls import path

from . import views

app_name = 'app'
urlpatterns = [
    path('', views.home, name='index'),
    path('home/', views.home, name='home'),
    path('home_2/', views.home_2, name='home2'),
    path('home_3/', views.home_3, name='home3'),
]