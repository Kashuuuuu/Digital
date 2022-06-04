from django.db import models


class Slider(models.Model):
    slider_image = models.ImageField()
    slider_text1 = models.TextField(max_length=500,null=True)  
    slider_text2 = models.TextField(max_length=500,null=True) 
    slider_text3 = models.TextField(max_length=500,null=True)  

class About(models.Model):
    icon = models.CharField(max_length=100)
    heading = models.CharField(max_length=500,null=True)  
    description = models.TextField(max_length=500,null=True) 

class Services(models.Model):
    icon = models.CharField(max_length=100)
    heading = models.CharField(max_length=500)  
    description = models.TextField(max_length=500)  

class Testimonial(models.Model):
    heading = models.CharField(max_length=500)
    image = models.ImageField()  
    description = models.TextField()
    subtext1 = models.TextField()
    subtext2 = models.TextField()
    icon1 = models.CharField(max_length=100)
    icon2 = models.CharField(max_length=100)
    icon3 = models.CharField(max_length=100)
    icon4 = models.CharField(max_length=100)
    icon5 = models.CharField(max_length=100)
     

           
