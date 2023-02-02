from django.contrib  import admin
from django.urls import include, path

from . import views

from django.urls import path
from . import views
app_name='bankapp'
urlpatterns = [
    path('home', views.home, name='home'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('newpage', views.newpage, name='newpage'),

    path('hh', views.hh, name='hh'),
   ]



