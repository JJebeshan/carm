from django.contrib import admin
from .models import Customer,Booking,invoice
# Register your models here.

admin.site.register(Customer)
admin.site.register(Booking)
admin.site.register(invoice)