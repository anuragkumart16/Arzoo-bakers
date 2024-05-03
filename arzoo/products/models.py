from django.db import models
from django.forms import ModelForm
# Create your models here.
import os

class popular(models.Model):
    upload = models.FileField(upload_to="uploads/")
    name = models.TextField(max_length=20)
    price = models.IntegerField(default=200)
    
    def __str__(self):
        return self.name
    
    def delete(self, *args, **kwargs):
        # Delete the associated file from the file system
        if self.upload:
            if os.path.isfile(self.upload.path):
                os.remove(self.upload.path)
        super().delete(*args, **kwargs)

class baked_and_ready(models.Model):
    upload = models.FileField(upload_to="uploads/")
    name = models.TextField(max_length=20)
    price = models.IntegerField(default=200)

    def __str__(self):
        return self.name
    
    def delete(self, *args, **kwargs):
        # Delete the associated file from the file system
        if self.upload:
            if os.path.isfile(self.upload.path):
                os.remove(self.upload.path)
        super().delete(*args, **kwargs)

