from django.contrib import admin
from .models import Contact

# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    #tuple
    list_display = ("id", "name", "email", "contact")


# Register to admin panel
admin.site.register(Contact, ContactAdmin)