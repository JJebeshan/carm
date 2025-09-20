from django.contrib import admin
from django.urls import path
from . import views



urlpatterns=[
    path('new',views.new, name="new"),
    path('close',views.close,name="close"),
    path('get_vehicle/',views.get_vehicle,name="get_vehicle"),
    path("send-otp/", views.sendotp, name="send_otp"),
    path("verify-otp/", views.verifyotp, name="verify_otp"),
    path("create", views.create, name="create"),
    path('get_customer/',views.get_customer,name="get_customer"),
    path('message',views.message,name="message"),
]