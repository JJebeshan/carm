from django.db import models

# Create your models here.
class add_user(models.Model):
    name=models.CharField(max_length=20)
    email=models.CharField(max_length=30)
    phone=models.CharField(max_length=12)
    password=models.CharField(max_length=15)
    p_address=models.CharField(max_length=15)
    
