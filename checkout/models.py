from datetime import datetime
from django.db import models
from django.contrib.auth.models import User
import datetime

from home.models import Home

class Cart(models.Model):
    user =models.ForeignKey(User, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False, null=True,blank=True)
    total_price = models.FloatField(default=0,null=True,blank=True)
    product =models.ForeignKey(Home, on_delete=models.CASCADE,null=True,blank=True)  
    price = models.FloatField(default=0,null=True,blank=True)
    total_items = models.IntegerField(default=0,null=True,blank=True)
    quantity = models.IntegerField(default=1,null=True,blank=True) 


class myCart(models.Model):
    user =models.ForeignKey(User, on_delete=models.CASCADE)
    productid=models.IntegerField()
    quantity = models.IntegerField() 
    def __str__(self):
        return self.user.username +' '+ str(self.productid) + ' '+ str(self.quantity)

class checkout(models.Model):

    user =models.ForeignKey(User, on_delete=models.CASCADE)
    productid=models.IntegerField(null=True)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField()
    date=models.DateField(default=datetime.datetime.today)
    email = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=150)
    phone = models.IntegerField()

   
    

