from django.contrib import admin
from .models import *

# Register your models here.
class cartAdmin(admin.ModelAdmin):
    pass

admin.site.register(Cart, cartAdmin)