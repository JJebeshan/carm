from django.contrib import admin
from django.urls import path
from . import views

urlpatterns=[
    path('registration',views.branch_regsitration,name="registration"),
    path('adduser',views.add_user,name="adduser")
]