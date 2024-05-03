from django.db import models
import os
# Create your models here.
class customorder(models.Model):
    
    description=models.TextField(max_length=500)
    refimage=models.FileField(upload_to='uploads/', null=True)
    reflink=models.TextField(max_length=200,null=True)
    name=models.CharField(max_length=50,default='none')
    phone=models.TextField(max_length=12)
    address=models.TextField(max_length=300)

    def __str__(self):
        return self.name
    
    def delete(self, *args, **kwargs):
        # Delete the associated file from the file system
        if self.refimage:
            if os.path.isfile(self.refimage.path):
                os.remove(self.refimage.path)
        super().delete(*args, **kwargs)