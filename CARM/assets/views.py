from django.contrib import messages
from django.shortcuts import render,redirect ,get_object_or_404
from django.http import HttpResponse,JsonResponse
# Create your views here.
def declaration(request):

    return render(request,'Assets/declaration.html')
def pricing(request):

    return render(request,'Assets/vehicle_registration.html')

def maintaince(request):

    return render(request,'Assets/vehicle_maintaince.html')
