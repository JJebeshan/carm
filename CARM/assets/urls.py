from django.urls import path
from . import views


urlpatterns=[
    path('declaration',views.declaration,name="declaration"),
    path('pricing',views.pricing,name="pricing"),
    path('maintaince',views.maintaince,name="maintaince"),
    path('check_availability',views.check_availability,name="check_availability"),
    path("get_purchase/", views.get_purchase, name="get_purchase"),

]

