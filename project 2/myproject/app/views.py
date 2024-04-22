from django.shortcuts import render,redirect
from django.http import HttpResponse
from . models import *
from django.contrib.auth.hashers import make_password
# Create your views here.
def index(request):
    return render(request, "index.html")

def create_user(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        password = make_password(request.POST['psssword'])
        if User.objects.filter(email=email).exists():
            return HttpResponse("Email Already Exists")
        else:
            User.objects.create(name=name,email=email,password=password)
            return redirect('/')
    

def table(request):
    users=User.objects.all()
    return render(request, "table.html",{"users":users})

def delete(request,pk):
    User.objects.get(id=pk).delete()
    return redirect('/data/')

def update_user(request,uid):
    user_obj=User.objects.get(id=uid)
    return render(request, "update.html", {"user_obj":user_obj})

def update_data(request):
    if request.method =="POST":
        uid=request.POST['uid']
        name=request.POST['name']
        email=request.POST['email']
        User.objects.filter(id=uid).update(name=name, email=email)
        return HttpResponse("User Update Sucessfully")