"""digital URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from dashboard import views

urlpatterns = [
  path('dashboard/',views.dashboard, name='dashboard'),
  path('products/',views.products, name='products'),
  path('datatable/',views.datatable, name='datatable'),
  path('checkouttable/',views.checkouttable, name='checkouttable'),
  path('delete_product/',views.delete_product, name='delete_product'),
  path('addproduct',views.addproduct , name='addproduct'),
#   path('edit/<int:pk>/',views.edit , name='edit'),
#   path('delete/<int:pk>/',views.delete , name='delete'),
  path('aboutus/',views.aboutus, name='aboutus'),
  path('service/',views.service, name='service'),
#   path('testi/',views.testi, name='testi'),
#   path('add_product/',views.add_product, name='add_product'),
#   path('editabout/',views.editabout, name='editabout'),
  path('add_about/',views.add_about, name='add_about')    

  










]
