from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('musicat', views.musicat, name='musicat'),
    path('upload/', views.upload, name='upload')
]