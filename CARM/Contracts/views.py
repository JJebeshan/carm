from django.shortcuts import render,redirect,HttpResponse,HttpResponseRedirect
def new(request):
    return render(request,'Contract/Create.html')

# Create your views here.
