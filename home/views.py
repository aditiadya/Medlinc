from django.shortcuts import render

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

def bookanapointment(request):
    return render(request, 'bookanapointment.html')