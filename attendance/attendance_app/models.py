from django.db import models

#from pname4 import attendance

# Create your models here.

class Students(models.Model):
    First_name = models.CharField(max_length=100)
    Last_name = models.CharField(max_length=100)
    #request=models.CharField(max_length=100)
    attendance = models.BooleanField(default=False)