from django.contrib import admin
from django.urls import path
from . import views



urlpatterns=[
    path('new',views.new, name="new"),
    path('close',views.close,name="close"),
    path('get_vehicle/',views.get_vehicle,name="get_vehicle")
]