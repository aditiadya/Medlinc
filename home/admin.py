from django.contrib import admin
from .models import Contact, Enquiry, Signup

# Register your models here.
# using this we allow only selected model to show to the admin 
# class ContactAdmin(admin.ModelAdmin):
    # fields = ('name', 'phone')

# admin.site.register(Contact, ContactAdmin)

admin.site.register(Contact)
admin.site.register(Enquiry)
admin.site.register(Signup)
