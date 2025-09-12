from django.urls import path
from . import views

urlpatterns=[
    path('declaration',views.declaration,name="declaration"),
    path('pricing',views.pricing,name="pricing"),
    path('maintaince',views.maintaince,name="maintaince"),

]