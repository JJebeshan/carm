from django.shortcuts import render,redirect,HttpResponse,HttpResponseRedirect
from django.http import JsonResponse
from assets.models import Vehicle_listing

def get_vehicle(request):
    ast_code = request.GET.get("Plate_no")
    try:
        asset = Vehicle_listing.objects.get(Plate_no=ast_code)
        return JsonResponse({"color": asset.color,"brand":asset.brand,"model":asset.model, "Rent":asset.Rent, "meeter":asset.meter_In})
    except Vehicle_listing.DoesNotExist:
        return JsonResponse({"purchase": None})
    
def new(request):
    vehicle=Vehicle_listing.objects.all()

    if request.method=='POST':
        date=request.POST.get('docdate')


    return render(request,'Contract/Create.html',{"vehicle":vehicle})

def close(request):
    return render(request,'Contract/close.html')
