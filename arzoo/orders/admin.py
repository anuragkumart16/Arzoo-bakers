from django.contrib import admin
from .models import *
# Register your models here.

class customorderAdmin(admin.ModelAdmin):
    pass

admin.site.register(customorder, customorderAdmin)