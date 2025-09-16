from django.db import models

# Create your models here.
class staff(models.Model):
    Name=models.CharField(max_length=25)
    email=models.EmailField(max_length=50)
    phone=models.CharField(max_length=12)
    userid=models.CharField(max_length=8)
    password=models.CharField(max_length=20)
    T_street=models.CharField(max_length=50)
    T_District=models.CharField(max_length=30)
    T_pincode=models.CharField(max_length=6)
    P_street=models.CharField(max_length=50)
    p_District=models.CharField(max_length=30)
    p_pincode=models.CharField(max_length=6)
    Account_number=models.CharField(max_length=30)
    Bank_name=models.CharField(max_length=100)
    Ifsc=models.CharField(max_length=12)
    Position=models.CharField(max_length=4)
    permission=models.CharField(max_length=8)

    def __str__(self):
        return self.userid
    class meta:
        verbose_name='User'
        db_table='users'
        ordering=['userid']




