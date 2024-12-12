from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name= 'calculator-home'),
    path('calculate/', views.calculate, name= 'calculate'),
]
