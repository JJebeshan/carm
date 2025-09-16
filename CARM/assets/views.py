from django.contrib import messages
from django.shortcuts import render,redirect ,get_object_or_404
from django.http import HttpResponse,JsonResponse
from .models import Asset_register,Vehicle_listing,maintaince
from django.shortcuts import render, redirect
from .forms import AssetRegisterForm , VehicleForm

def declaration(request):
    if request.method == "POST":
        form = AssetRegisterForm(request.POST, request.FILES)
        if form.is_valid():
            asset = form.save(commit=False)
            asset.addedby = request.session['userid']  # if using auth user
            asset.save()
            return redirect("declaration",)  # reload with success message
    else:
        form = AssetRegisterForm()

    return render(request, "Assets/declaration.html", {"form": form})


def check_availability(request):
    asset_code=request.GET.get("code","")
    exists=Asset_register.objects.filter(Ast_code=asset_code).exists()
    return JsonResponse({"available":not exists})

def get_purchase(request):
    ast_code = request.GET.get("ast_code")
    try:
        asset = Asset_register.objects.get(Ast_code=ast_code)
        return JsonResponse({"purchase": asset.Ast_Price,"brand":asset.Ast_Brand,"model":asset.Ast_Model})
    except Asset_register.DoesNotExist:
        return JsonResponse({"purchase": None})
    

def pricing(request):
    if request.method == "POST":
        vehicle_form = VehicleForm(request.POST, request.FILES)

        if vehicle_form.is_valid():
            # Don't commit yet
            vehicle = vehicle_form.save(commit=False)

            # Auto-fill Purchase from Asset_register
            ast_code = vehicle_form.cleaned_data.get("Ast_code")
            if ast_code:
                asset = get_object_or_404(Asset_register, Ast_code=ast_code)
                vehicle.Purchase = asset.Ast_Price
                vehicle.model = asset.Ast_Model
                vehicle.brand = asset.Ast_Brand
            vehicle.save()

            return redirect("dashboard")  # Use your URL name here
        else:
            print(vehicle_form.errors)               # 🔍 This shows why it fails
            return HttpResponse(vehicle_form.errors)

        # If invalid, fall through and render with errors
    else:
        vehicle_form = VehicleForm()
    return render(request, "Assets/vehicle_registration.html", {
        "vehicle_form": vehicle_form
    })


    



def maintaince(request):

    return render(request,'Assets/vehicle_maintaince.html')
