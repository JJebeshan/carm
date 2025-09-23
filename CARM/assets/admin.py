from django.contrib import admin
from .models import Asset_register,Vehicle_listing,maintaince,CarLocation

admin.site.register(Asset_register)
admin.site.register(Vehicle_listing)
admin.site.register(maintaince)
admin.site.register(CarLocation)

