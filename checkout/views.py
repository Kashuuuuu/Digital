
from atexit import register
from re import template
from telnetlib import PRAGMA_HEARTBEAT
from django.urls import path,include
from django.shortcuts import redirect, render
from django.http import HttpResponse,HttpResponseRedirect
from django.views import View
from home.models import Home
from checkout.models import *
from checkout.models import checkout
from django.shortcuts import (get_object_or_404)

# register = template.Library()


# @register.filter(name='currency')
# def currency(number):#     return '₹'+str(number) 

# Create your views here.
# def checkout(request):
#     return render(request,"checkout.html")

def summary(request):
    return render(request,"checkout.html")

def cart(request):
    prod =request.GET.get('cart')    # value from cart
    # remove = request.POST.get('remove')
   
    user=User.objects.get(id=request.user.id )
    
    crt=myCart.objects.filter(productid=prod,user=user)
    quantity = 0
    if prod!=None:
        if len(crt)>0:
            ob=crt[0]
            ob.quantity+=1
            ob.save()
        else: 
            crts=myCart(user=User.objects.get(id=request.user.id),productid=prod,quantity=1)
            crts.save()

     
    crts=myCart.objects.filter( user=User.objects.get(id=request.user.id))
    li=[]
    tot=0
    totalprice=0
    for i in crts:
        prods=Home.objects.filter(id=i.productid)
        prod=Home.objects.get(id=i.productid)
        price=prod.item_price*i.quantity
        tot+=int(price)
        li.append([prods,tot,i.quantity])
        totalprice = (totalprice+prod.item_price) + (prod.item_price *i.quantity )
    res={'data':li,
        'totalprice':totalprice}  



    return render(request,"cart.html",res)




def checkouts(request):
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
        totalprice = (totalprice+prod.item_price) + (prod.item_price *i.quantity )
    res={'list':li,
           'totalprice':totalprice } 
    
    print('llliii',request.method, request.GET.get('email'))
    for i in crts:
        if request.method == 'POST':   
            print(request.method,'//', request.POST.get('email')) 
            mail = request.POST.get('email')
            name = request.POST.get('name')
            address =request.POST.get('address')
            phone = request.POST.get('phone')
            user=User.objects.get(id=request.user.id)
            cart =request.GET.get('cart')
            product=Home.objects.get(id=i.productid)
           
            data = checkout(email=mail,name=name,address=address,phone=phone ,
                            user=User.objects.get(id=request.user.id),
                            productid=product.id,price=product.item_price,quantity=i.quantity)  
            obj = myCart.objects.filter(id=request.user.id,productid=product.id)
            obj.delete()                
            data.save()      
  

    return render(request,"checkout.html",res)





def delete(request):
    prod =request.GET.get('rm')
    obj = myCart.objects.filter(user=User.objects.get(id=request.user.id),productid = prod)
    print(obj)
    
    obj.delete()
        
    return redirect('checkout')





def update(request):
    prod =request.GET.get('min')
    
    prod1 =request.GET.get('mix')

    crt=myCart.objects.filter(productid=prod,user=request.user.id)
    
    crt1=myCart.objects.filter(productid=prod1,user=request.user.id)
    print(prod,'pp',crt)
    if prod!=None:
        # print(prod,'//')
        if len(crt)>0:
            ob=crt[0]
            ob.quantity-=1
            ob.save()
    elif prod1!=None:
        if len(crt1)>0:
            ob=crt1[0]
            ob.quantity+=1
            ob.save()
    else: 
        crts=myCart(user=User.objects.get(id=request.user.id),productid=prod,quantity=1)
        crts.save()


    return redirect('cart')

def payment(request):
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
        totalprice = (totalprice+prod.item_price) + (prod.item_price *i.quantity )
       

    res={'list':li,
           'totalprice':totalprice } 
    return render(request,"payment.html",res)   
    







    