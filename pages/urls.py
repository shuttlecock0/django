from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('dinner/', views.dinner),
    path('hello/<name>/', views.hello),
    path('introduce/<name>/<age>/', views.introduce),
    path('times/<int:num1>/<int:num2>/', views.times),
    path('area/<int:r>/', views.area),
]
