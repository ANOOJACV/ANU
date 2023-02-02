from django.shortcuts import render,redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404
from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import  CreateView, UpdateView
from django.urls import reverse_lazy
from django.shortcuts import render


# Create your views here.
#  def index(request):
#     return HttpResponse('bank')
def home(request):
    return render(request,"home.html")
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if User is not None:
            auth.login(request,user)
            return redirect('/')

        else:
            messages.info(request, "invalid credentials")
            return redirect('login')
    else:

        return render(request, "login.html")
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['password1']
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
                return redirect('/')
            else:
                user = User.objects.create_user(username=username, password=password)

                user.save()
                return redirect('login.html')
        else:
            messages.info(request, "password not matching")
            return redirect('register.html')
    else:
        return render(request, "register.html")
def newpage(request):
    return render(request,"newpage.html")






def hh(request):
    return render(request,"hh.html")

