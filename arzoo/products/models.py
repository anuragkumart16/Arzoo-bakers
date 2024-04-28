from django.db import models
from django.forms import ModelForm
# Create your models here.

class popular(models.Model):
    upload = models.FileField(upload_to="uploads/")
    name = models.TextField(max_length=20)
    
    def __str__(self):
        return self.name

class baked_and_ready(models.Model):
    upload = models.FileField(upload_to="uploads/")
    name = models.TextField(max_length=20)

    def __str__(self):
        return self.name

class popularform(ModelForm):
    model = popular
    fields =['upload','name']

class baked_and_readyform(ModelForm):
    model = baked_and_ready
    fields =['upload','name']