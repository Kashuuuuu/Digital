from django.contrib import admin

from home.models import Home

class Product_Admin(admin.ModelAdmin):
    list = ('item_name','item_desc','item_tag','item_version','image_size','item_filesincluded',
    'item_documentation','item_license','item_price','item_image',)

class About_Admin(admin.ModelAdmin):
    list3 = ('icon','heading','description') 

admin.site.register(Home,Product_Admin)

