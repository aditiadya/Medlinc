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
    path('enquiry',views.enquiry, name="enquiry"),
    path('contact',views.contact, name="contact"),
    path('login',views.login, name="login"),
    path('sap',views.sap, name="sap"),
    path('signin',views.signin, name="signin"),
    path('reports',views.reports, name="reports"),
    path('medicines',views.medicines, name="medicines"),
    path('payment',views.payment, name="payment"),
    path('sos',views.sos, name="sos"),
    path('vc',views.vc, name="vc"),
    path('cart',views.cart, name="cart"),
]