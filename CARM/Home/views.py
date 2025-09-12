from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')

def login(request):
    return render(request,'Registration/login.html')

def company(request):
    return render(request,'Registration/company.html')

def dashboard(request):
    return render(request,'User/dashboard.html')