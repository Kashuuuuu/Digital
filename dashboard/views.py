from email import message
from urllib import request
from wsgiref.util import request_uri
from django.shortcuts import redirect, render
from home.models import Home
from django.contrib.auth.models import User 
import datetime
from checkout.models import checkout
from checkout.models import myCart
import os
from .forms import ProductForm
from dashboard.models import About, Services,Testimonial




# Create your views here.

def dashboard(request):
    product_data = Home.objects.all().order_by('item_name')[:10]

    data = {'product_data':product_data}
    return render(request,"dashboard.html",data)


def products(request):
    product_data = Home.objects.all()

    if request.method=='POST':
        prods = request.POST.get('delete')
        prod = request.POST.get('edit')
        if prods!=None: 
           prods=Home.objects.filter(id=prods)
           prods.delete()
            # message.success(request,'Product Deleted SuccessFully.')
           return redirect('products')
        # prod = request.POST['edit']
        elif prod!= None:
           image=request.POST['image']
           tag=request.POST['tag']
           desc=request.POST['desc']

           prod = Home.objects.filter(id=prod)

           if len(prod)>0:
                ob=prod[0] 
                if len(image)>0:
                    ob.item_image=image
                if len(tag)>0:
                    ob.item_tag=tag
                if len(desc)>0:
                    ob.item_desc=desc
                    ob.save()
                    # message.success(request,'Product Updated.')
                return redirect('products') 
                  

    data = {'product_data':product_data}
    return render(request,"products.html",data) 

   

def datatable(request):
    data = User.objects.all()

    d = {'data':data}

    return render(request,"datatables.html",d) 

def checkouttable(request):
    crts=myCart.objects.filter( user=User.objects.get(id=request.user.id))
    li=[]
    tot=0
    totalprice=0
    print(crts)
    for i in crts:
        prods=Home.objects.filter(id=i.productid)
        prod=Home.objects.get(id=i.productid)
        price=prod.item_price*i.quantity
        tot+=int(price)
        li.append([prods,tot,i.quantity])
        totalprice = totalprice + price
    res={'list':li,
           'totalprice':totalprice } 

    return render(request,"checkout_table.html",res)  

def delete_product(request):
   product_data = Home.objects.filter(id=name)
   if request.method=='POST':
    name=request.POST['itemname']
    prod = Home.objects.filter(id=name)
    print(prod)
    prod.delete
    data = {'product_data':product_data}
    return redirect('products') 





def addproduct(request):
    form = ProductForm()

    if request.method == 'POST':
        form = ProductForm(request.POST , request.FILES)
        if form.is_valid():
            form.save()
            return redirect('products')
    context = {
        'form':form
    }      
    return render(request,"addproduct.html",context)    

# def edit(request,pk):
#     product = Home.objects.get(id=pk)
#     form = ProductForm(instance=product)

#     if request.method == 'POST':
#         form = ProductForm(request.POST , request.FILES , instance=product)
#         if form.is_valid():
#             form.save()
#             return redirect('products')
  
#     context = {
#         'form':form
#     }      
#     return render(request,"edit.html",context)  


# def delete(request,pk):
#     product = Home.objects.get(id=pk)
#     product.delete()
#     return redirect('products')
          

def aboutus(request):
    about_data = About.objects.all()
    abt= request.POST.get('addabout')
    
    dl= request.POST.get('deleteabout')
    print(abt , dl)
       
    ed= request.POST.get('editabout')
    if request.method == "POST":
        if abt!=None:
            icon=request.POST['icon']
            heading=request.POST['heading'] 
            description=request.POST['description'] 
            About(icon=icon,heading=heading,description=description).save()
            return redirect('aboutus')  
        elif dl!=None: 
            prods=About.objects.filter(id=dl)
            prods.delete()
                # message.success(request,'Product Deleted SuccessFully.')
            return redirect('aboutus')  
        elif ed!=None:
                icon=request.POST['icon']
                heading=request.POST['heading']
                description=request.POST['description']

                prod = About.objects.filter(id= ed)

                if len(prod)>0:
                    ob=prod[0] 
                    if len(icon)>0:
                        ob.icon=icon
                    if len(heading)>0:
                        ob.heading=heading
                    if len(description)>0:
                        ob.description=description
                        ob.save()   

                        return redirect('aboutus')              

    data = {'about_data':about_data}
    return render(request,'aboutus.html',data)


  

def service(request):
    service_data = Services.objects.all()
    testi_data = Testimonial.objects.all()
    data = {'service_data':service_data,
            'testi_data':testi_data}
    return render(request,'service.html',data)

def add_about(request):
    if request.method == "POST":
        icon=request.POST['icon']
        heading=request.POST['heading'] 
        description=request.POST['description'] 
        About(icon=icon,heading=heading,description=description).save()
       
    return render(request,"aboutus.html")    

# def testi(request):
#     testi_data = Services.objects.all()
#     data = {'testi_data':testi_data}
#     return render(request,'service.html',data)    

       
      

        

                  
            