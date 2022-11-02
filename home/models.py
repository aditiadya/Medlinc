from cgi import print_arguments
from datetime import date, datetime
import email
from enum import auto
from pyexpat import model
from unittest.util import _MAX_LENGTH
from django.db import models
from importlib.resources import contents
# from sqlite3 import Timestamp
from statistics import mode
from unicodedata import name
from django.db import models
from numpy import True_

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


     

class Signup(models.Model):
     sno = models.AutoField(primary_key=True)
     name = models.CharField(max_length=200, null=True)
     email = models.CharField(max_length=200, null=True)
     password = models.CharField(max_length=100, null=True)
     confirmpassword = models.CharField(max_length=100, null=True)