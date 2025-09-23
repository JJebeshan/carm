from django.db import models
# Create your models here.

def asset_document_path(instance, filename):
    # Store files in media/assets/<Ast_code>/<filename>
    return f"assets/{instance.Ast_code}/{filename}"

class Asset_register(models.Model):
    Ast_code=models.CharField(max_length=50, primary_key=True)
    Ast_Type=models.CharField(max_length=30)
    Ast_Brand=models.CharField(max_length=30)
    Ast_Model=models.CharField(max_length=30)
    Ast_Isrent=models.BooleanField(default=True)
    Ast_Price=models.IntegerField()
    Ast_document = models.FileField(upload_to='documents/', null=True, blank=True)
    addedby=models.CharField(max_length=20 ,null=True, blank=True)

    def __str__(self):
        return self.Ast_code


class Vehicle_listing(models.Model):
    Ast_code = models.ForeignKey('Asset_register', on_delete=models.CASCADE,related_name='vehicles')
    Plate_no = models.CharField(max_length=50,primary_key=True)
    brand=models.CharField(max_length=30,null=True, blank=True)
    model=models.CharField(max_length=30,null=True, blank=True)
    Vehicle_type = models.CharField(max_length=10)
    Engine_type = models.CharField(max_length=6)
    Fuel_type = models.CharField(max_length=8)
    color = models.CharField(max_length=10)
    year = models.CharField(max_length=4)
    mileage = models.IntegerField()
    Purchase=models.IntegerField()
    Insurance=models.CharField(max_length=25)
    chasis_no=models.CharField(max_length=30)
    Engine_no=models.CharField(max_length=50)
    Rent=models.IntegerField()
    meter_In=models.IntegerField() 
    Front_image = models.ImageField(upload_to='vehicle_images/', null=True, blank=True)
    Back_image = models.ImageField(upload_to='vehicle_images/', null=True, blank=True)

    def __str__(self):
        return f"{self.Plate_no}"

class maintaince(models.Model):
    vehicle_no=models.ForeignKey(Vehicle_listing,on_delete=models.CASCADE)
    Reason=models.CharField(max_length=20)
    Expense=models.IntegerField()
    Description=models.TextField()
    Document=models.FileField(upload_to="maintaince/", null=True, blank=True)

    def __str__(self):
        return self.vehicle_no
    
class CarLocation(models.Model):
    car = models.ForeignKey(Vehicle_listing, on_delete=models.CASCADE)
    latitude = models.FloatField()
    longitude = models.FloatField()
    timestamp = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return f"{self.car.name} at {self.latitude},{self.longitude}"

