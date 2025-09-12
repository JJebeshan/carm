from django.shortcuts import render,redirect,HttpResponse,HttpResponseRedirect

# Create your views here.
def branch_regsitration(request):
    return render(request,'Registration/branch.html')

def add_user(request):
    return render(request,'user/adduser.html')