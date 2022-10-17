from django.db import models
from importlib.resources import contents
from sqlite3 import Timestamp
from statistics import mode
from unicodedata import name
from django.db import models

# Create your models here.
class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=15)
    email  = models.CharField(max_length=200)
    content = models.TextField()
    Timestamp = models.DateTimeField(auto_now_add=True, blank=True)

class Enquiry(models.Model):
     sno = models.AutoField(primary_key=True)
     name = models.CharField(max_length=200)
     phone = models.CharField(max_length=15)
     email  = models.CharField(max_length=200)
     content = models.TextField()

class signup(models.Model):
     sno = models.AutoField(primary_key=True)
     name = models.CharField(max_length=200)
     email  = models.CharField(max_length=200)
     password  = models.CharField(max_length=200)
     


    
     