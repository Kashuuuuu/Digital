from django.http import HttpResponseRedirect
from django.shortcuts import render
from home.models import Home
from dashboard.models import About,Services,Testimonial




# Create your views here.
def index(request):
    
    product_data = Home.objects.all().order_by('item_name')[:3]
    about_data = About.objects.all()
    service_data = Services.objects.all()
    testi_data = Testimonial.objects.all()

    data = {'product_data':product_data ,
             'about_data':about_data ,
             'service_data':service_data,
             'testi_data':testi_data
              }


    return render(request,"index.html",data)







 

    