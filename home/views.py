from email import message
from email.headerregistry import Address
from unicodedata import name
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib import messages
from .models import Contact, Enquiry, Signup
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    return render(request, 'index.html')

def base(request):
    return render(request, 'base.html')

def maxhome(request):
    return render(request, 'maxhome.html')

def maxlab(request):
    return render(request, 'maxlab.html')

def healthcheckup(request):
    return render(request, 'healthcheckup.html')



def vc(request):
    return render(request, 'vc.html')



def login(request):
    return render(request, 'login.html')

def reports(request):
    return render(request, 'reports.html')

def medicines(request):
    return render(request, 'medicines.html')

def payment(request):
    return render(request, 'payment.html')

def sos(request):
    return render(request, 'sos.html')

def cart(request):
    return render(request, 'cart.html')

# contact
def contact(request):
    # messages.success(request, 'Welcome To Contact')
    if request.method=='POST':
        name = request.POST.get('name', '')
        phone = request.POST.get('phone', '')
        email = request.POST.get('email', '')
        content = request.POST.get('content', '')
        contact = Contact(name=name, email=email, phone=phone, content=content)
        print(name, email, phone, content)
        contact.save()
        messages.success(request, "Thank You For Choosing Us!")
        return redirect("/contact")
    return render(request, 'contact.html')

    # Enuiry 
def enquiry(request):
    # messages.success(request, 'Welcome To Contact')
    if request.method=='POST':
        name = request.POST.get('name', '')
        phone = request.POST.get('phone', '')
        email = request.POST.get('email', '')
        content = request.POST.get('content', '')
        enquiry = Enquiry(name=name, email=email, phone=phone, content=content)
        print(name, email, phone, content)
        enquiry.save()
        messages.success(request, "Enquiry Send Successfully!")
        return redirect("/enquiry")
    return render(request, 'enquiry.html')

def bookanapointment(request):
    return render(request, 'bookanapointment.html')

# sign up as patient 
def sap(request):
    # messages.success(request, 'Welcome To Contact')
    if request.method=='POST':
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        confirmpassword = request.POST['confirmpassword']

        if not name.isalnum():
            messages.error(request, "Username should only contain letter and numbers.")
            return redirect('/sap')

        if password != confirmpassword:
            messages.error(request, "Passwords do not match")
            return redirect('/sap')

        myuser = Signup.objects.create(name=name, email=email, password='*****', confirmpassword="*****")
        myuser.save()
        messages.success(request, "Sign Up Successfully!")
        return redirect("/sap")
    return render(request, 'sap.html')
    # else:
        # return HttpResponse('404 - Not Found')

def signin(request):

    return render(request, 'signin.html')