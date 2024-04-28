from django.contrib import admin
from .models import *

class popularAdmin(admin.ModelAdmin):
    pass
class baked_and_readyAdmin(admin.ModelAdmin):
    pass

admin.site.register(popular, popularAdmin)
admin.site.register(baked_and_ready,baked_and_readyAdmin)

