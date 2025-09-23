from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.utils import timezone
from datetime import timedelta
from .models import Users_log
from assets.models import Vehicle_listing,Asset_register
# Create your views here.
def index(request):
    vehicle=Vehicle_listing.objects.all()

    return render(request,'index.html',{'vehicles':vehicle})

def login(request):
    return render(request,'Registration/login.html')

def logout(request):
    request.session.flush()
    return redirect('login')

def company(request):
    return render(request,'Registration/company.html')

def user_verify(request):
    if request.session.get('userid'):
        return render(request,"User/dashboard.html")
    return redirect('dashboard')

def dashboard(request):
    if request.method == 'POST':
        Userid = request.POST.get('userid')
        password = request.POST.get('password')

        try:
            user = Users_log.objects.get(userid=Userid)
        except Users_log.DoesNotExist:
            return HttpResponse("Invalid User ID")

        # Check lock
        if user.is_locked():
            return HttpResponse("Account locked. Try again after 24 hours.")

        if user.password == password:
            # Reset failed attempts
            user.reset_attempt()

            # Check role
            if user.role == "admin":
                request.session['userid']=Userid
                request.session['role']=user.role
                return render(request, "User/dashboard.html", {"user": user})
            elif user.role == "staff":
                request.session['userid']=Userid
                request.session['role']=user.role
                return render(request, "User/dashboard.html", {"user": user})
            else:
                return render(request, "User/dashboard.html", {"user": user})

        else:
            user.failed_attempts += 1
            if user.failed_attempts >= 3:
                user.lock_until = timezone.now() + timedelta(hours=24)
            user.save()
            return HttpResponse("Invalid Credentials")

    return redirect('login')
