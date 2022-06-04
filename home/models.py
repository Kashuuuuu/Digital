from trace import Trace
from django.db import models
from django.forms import IntegerField
from django.contrib.auth.models import User



class Home(models.Model):
    item_name  = models.CharField(max_length=50)
    item_desc  = models.TextField()
    item_tag  = models.CharField(max_length=100)
    item_version  = models.CharField(max_length=50)
    item_filesincluded  = models.CharField(max_length=50)
    item_documentation  = models.CharField(max_length=50)
    item_license  = models.CharField(max_length=50)
    item_price  = models.CharField(max_length=150)
    item_image = models.ImageField()





    
    

    

