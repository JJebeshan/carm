from django.db import models
# Create your models here.

class Customer(models.Model):
    customer_id=models.CharField(max_length=10)
    name=models.CharField(max_length=50)
    mobile=models.CharField(max_length=12)
    email=models.CharField(max_length=50)

    def __str__(self):
        return self.id

class Booking(models.Model):
    Docno=models.CharField(max_length=10,primary_key=True)
    Docdate=models.DateField()
    Vehicle=models.CharField(max_length=50)
    Booking_Status=models.CharField(max_length=10)
    Meter_out=models.IntegerField()
    Meter_in=models.IntegerField(null=True,blank=True)
    Rent=models.IntegerField()
    Allowed_km=models.IntegerField()
    Add_km=models.IntegerField()
    Latehour=models.IntegerField()
    Total_Days=models.IntegerField()
    timein=models.DateField(blank=True, null=True)
    Customer_id=models.ForeignKey(Customer,on_delete=models.SET_NULL, null=True, blank=True)
    Discount_type=models.CharField(max_length=8)
    Discount_value=models.IntegerField()
    Tax_type=models.CharField(max_length=10)
    Tax=models.IntegerField()
    Deposit=models.IntegerField(default=0)
    service=models.CharField(max_length=10, null=True,blank= True)
    service_charge=models.IntegerField(blank=True,null=True)
    others_Type=models.CharField(max_length=20)
    others_price=models.IntegerField()
    Reciept=models.IntegerField()
    payment_method=models.CharField(max_length=10, blank=True,null=True)
    Payment_docno=models.IntegerField(default=0)
    Total_exclude=models.IntegerField(default=0)
    Total_include=models.IntegerField(default=0)
    Balance=models.IntegerField(default=0)
    

    def __str__(self):
        return self.Docno


class invoice(models.Model):
    invno=models.CharField(max_length=10)
    bookno=models.ForeignKey(Booking, on_delete=models.CASCADE)
    Docdate = models.DateTimeField(auto_now_add=True)
    totalrent=models.IntegerField()
    totalothers=models.IntegerField()
    addkm=models.IntegerField()
    latehour=models.IntegerField()
    totaltax=models.IntegerField()
    discount=models.IntegerField()
    payment=models.IntegerField()
    method=models.IntegerField()
    balance=models.IntegerField()

    def __str__(self):
        return self.invno