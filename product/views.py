from django.shortcuts import render
from home.models import Home


# Create your views here.
def product(request):
    prod=request.GET.get('product')
    
    product_data = Home.objects.filter(id=prod)
    return render(request,"product.html",{'product_data':product_data})
