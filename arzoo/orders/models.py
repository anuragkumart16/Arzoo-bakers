from django.db import models

# Create your models here.
class customorder(models.Model):
    
    description=models.TextField(max_length=500)
    refimage=models.FileField(upload_to='uploads/')
    reflink=models.TextField(max_length=200)
    name=models.CharField(max_length=50,default='none')
    phone=models.TextField(max_length=12)
    address=models.TextField(max_length=300)

    def __str__(self):
        return self.name