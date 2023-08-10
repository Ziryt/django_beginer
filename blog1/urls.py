from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-homie'),
    path('about/', views.about, name='blog-about')
]
