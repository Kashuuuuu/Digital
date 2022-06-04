
from django.urls import path,include
from django.shortcuts import redirect, render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
import uuid
import socket
socket.getaddrinfo('localhost', 8080)
from .models import *

from django.core.mail import send_mail

from django.conf import settings
# Create your views here.
def signin(request):

        if request.method == 'POST':
            email = request.POST['email']
            password = request.POST['password']
          
            name = User.objects.get(email=email).username
            user = authenticate(username=name, password=password)
            print('user')
            if user is not None:
                login(request, user)
                return render(request,"shop.html")
            else:  
                messages.success(request,"error please try again")  
                return render(request,"signup.html")

        return render(request,"signin.html") 
        
      

def signup(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        repassword = request.POST.get('repassword')
        data = User.objects.create_user(username=name,email=email,password=password)
        data.save()
        profile_obj = Profile(user=data,forgot_password_token=str(uuid.uuid4()))
            # profile_obj.forgot_password_token = token
        profile_obj.save()
        messages.success(request,"You registered successfully..")

    return render(request,"signup.html")    

def forgot(request):
    if request.method =='POST':
        email=request.POST.get('email')

        if not User.objects.filter(email=email).first():
            messages.success(request,'no user found,please signup..')
            return render(request,"signup.html")

        else:
            user_email = User.objects.get(email=email)
            
            profile_obj = Profile.objects.get(user=user_email).forgot_password_token
         
           
            subject = 'your forgot password link'
            message = f'Hi,click on the link to reset your password http://127.0.0.1:8000/changepassword/{profile_obj}.'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [email]
            send_mail(subject,message,email_from,recipient_list)
            
            messages.success(request,'message sent successfully..')
            
    return render(request,"forgot.html")    

def changepassword(request , token):
    context={}
   
    profile_obj = Profile.objects.get(forgot_password_token=token)
    context ={'user_id' : profile_obj.user.id}


    if request.method == 'POST':
        new_pw = request.POST.get('newpassword')
        rp_pw = request.POST.get('repeat_password')
        user_id = request.POST.get('user_id')

        if user_id is None:
            messages.success(request,'userID not found')
            return render(request,"changepassword.html")

        if new_pw != rp_pw:
            messages.success(request,'password is not same')
            return render(request,"changepassword.html")

        user_email = User.objects.get(id=user_id)
        user_email.set_password(new_pw)
        user_email.save()
        messages.success(request,'password changed successfully')
        return render(request,"signin.html")

        return render(request,"signin.html")


        

    return render(request,"changepassword.html",context)     
