from django.shortcuts import render,redirect,HttpResponse,HttpResponseRedirect
from django.http import JsonResponse
from django.contrib import messages
from django.db import models 
import random
import json
from assets.models import Vehicle_listing
from . models import Customer, Booking, invoice
from django.utils.dateparse import parse_datetime,parse_date

#map tracking


def get_vehicle(request):
    ast_code = request.GET.get("Plate_no")
    try:
        asset = Vehicle_listing.objects.get(Plate_no=ast_code)
        return JsonResponse({"color": asset.color,"brand":asset.brand,"model":asset.model, "Rent":asset.Rent, "meeter":asset.meter_In})
    except Vehicle_listing.DoesNotExist:
        return JsonResponse({"purchase": None})
    
def get_customer(request):
    cust=request.GET.get("customer_id")
    try:
        cust_detail=Customer.objects.get(customer_id=cust)
        return JsonResponse({"name":cust_detail.name,"email":cust_detail.email,"phone":cust_detail.mobile})
    except Customer.DoesNotExist:
        return JsonResponse({"custid": None})
    
def new(request):
    active_vehicles=Booking.objects.filter(Booking_Status="Active").values_list("Vehicle",flat=True)
    vehicle = Vehicle_listing.objects.exclude(Plate_no__in=active_vehicles)
    customer=Customer.objects.all()
    last_customer=Customer.objects.order_by("id").last()
    if last_customer:
        last_num=last_customer.customer_id
        last_id=int(''.join(filter(str.isdigit,last_num)))
        newnum=last_id+1
        newid=f"CUST{newnum:03d}"
    else:
        newid="CUST001"
        
    if request.method=='POST':
        date=request.POST.get('docdate')


    return render(request,'Contract/Create.html',{"vehicle":vehicle,"Customer":customer,"Customerid":newid})

def create(request):
    if request.method=='POST':
        action=request.POST.get('action')
        doclast=Booking.objects.order_by("Docno").last()
        if doclast:
            docnew=int(str(doclast))+1
        else:
            docnew="1001"
        docno=str(docnew)
        docdate_str=request.POST.get('docdate')
        vehicle=request.POST.get('Plate_no')
        vehiclecode=Vehicle_listing.objects.get(Plate_no=vehicle)
        customer_type = request.POST.get('customerType')
        book_status='Active'
        customid_exist=request.POST.get('cust_id')
        customer_new=request.POST.get('custid')
        meterout=int(request.POST.get('meeter', 0))
        rent = int(request.POST.get('Rent', 0))
        Allowedkm = 300  # already an int
        add_km = int(request.POST.get('addkm', 0))
        late = int(request.POST.get('latehr', 0))
        totaldays = int(request.POST.get('days', 0))
        timein_str =request.POST.get('return_date')
        deposit = int(request.POST.get('deposit', 0))
        service_amount = int(request.POST.get('service_amount', 0))
        others = int(request.POST.get('other', 0))
        Total_execlude = int(float(request.POST.get('Excltax', 0)))
        Total_include = int(float(request.POST.get('incltax', 0)))
        credit = deposit  # already int
        Balance = int(float(request.POST.get('balance', 0)))
        disc_value = int(request.POST.get('amount', 0))
        disc_type=request.POST.get('disc_type')
        tax_type=request.POST.get('tax')
        services=request.POST.get('service')
        others_type=request.POST.get('other_type')
        paymentmethod=request.POST.get('paymethod')
        tax = int(request.POST.get('tax_amount', 0))
        docdate = parse_date(docdate_str)
        timein = parse_date(timein_str)
        if customer_type == 'existing':
            customer_cr = Customer.objects.get(customer_id=customid_exist)
        else:
            customer_cr = Customer.objects.get(customer_id=customer_new)
        payementdocno= int(str(random.randint(10000,99999)))
        newbooking = Booking.objects.create(
            Docno=docno,
            Docdate=docdate,
            Vehicle=vehiclecode,
            Booking_Status=book_status,
            Meter_out=meterout,
            Rent=rent,
            Allowed_km=Allowedkm,
            Add_km=add_km,
            Latehour=late,
            Total_Days=totaldays,
            timein=timein,
            Customer_id=customer_cr,  # Assuming you're passing customer_id directly
            Discount_type=disc_type,
            Discount_value=disc_value,
            Tax_type=tax_type,
            Tax=tax,
            Deposit=deposit,
            service=services,
            service_charge=service_amount,
            others_Type=others_type,
            others_price=others,
            Reciept=credit,  # You can define or calculate this
            payment_method=paymentmethod,  # Example: Add dynamically from POST if available
            Payment_docno=payementdocno,  # Example: Add dynamically from POST if available
            Total_exclude=Total_execlude,  # Add logic if you need it
            Total_include=Total_include,  # Add logic if you need it
            Balance=Balance  # Add logic if you need it
        )
    messages.success(request, "✅ Contract created successfully!")  

    return redirect('new')

def close(request):
    return render(request,'Contract/close.html')

def message(request):
    return render(request,'Contract/message.html')

def sendotp(request):
    if request.method=="POST":
        otp=str(random.randint(10000,99999))
        request.session['otp']=otp
        print(otp)
        return JsonResponse({"status": "success", "message": "OTP sent successfully!"})
    return JsonResponse({"status": "error", "message": "Invalid request"}, status=400)

def verifyotp(request):
    if request.method=="POST":
        enterotp=request.POST.get("otp")
        sessionotp=request.POST.get("otp")
        data = json.loads(request.body.decode("utf-8"))
        custid = data.get("custid")
        name = data.get("name")
        email = data.get("email")
        phone = data.get("phone")
        print(name, email, phone)

        last_customer = Customer.objects.order_by("id").last()
        if last_customer:
            last_id = int(last_customer.customer_id.replace("CUST", ""))
            cust_id = f"CUST{last_id + 1:03d}"
        else:
            cust_id = "CUST001"
        if enterotp == sessionotp:
            customer = Customer.objects.filter(models.Q(mobile=phone) | models.Q(email=email)).first()
            if not customer:
                customer = Customer.objects.create(customer_id=cust_id, name=name, mobile=phone, email=email )

            return JsonResponse({"status": "success", "message": "OTP sent successfully!"})
        return JsonResponse ({"status": "error", "message": "Invalid request"}, status=400)
    return JsonResponse ({"status": "error", "message": "Invalid request"}, status=400)
