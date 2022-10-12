from django.contrib import admin
from django.urls import URLPattern, path, include
from home import views

urlpatterns = [
    path('',views.index, name="home"),
    path('base',views.base, name="base"),
    path('maxhome',views.maxhome, name="maxhome"),
    path('maxlab',views.maxlab, name="maxlab"),
    path('healthcheckup',views.healthcheckup, name="healthcheckup"),
    path('bookanapointment',views.bookanapointment, name="bookanapointment"),

]