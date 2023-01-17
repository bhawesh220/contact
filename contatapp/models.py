
'''import required module'''
from django.db import models

# Create your models here.
class contactmodel(models.Model):
    sname=models.CharField(max_length=100)
    sroll=models.IntegerField()
    email=models.EmailField()




