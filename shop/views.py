from django.shortcuts import render
from home.models import Home


# Create your views here.
def shop(request):

    product_data = Home.objects.all()

    data = {'product_data':product_data}

    return render(request,"shop.html",data)   