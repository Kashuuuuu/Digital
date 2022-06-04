from django.contrib import admin

from checkout.models import Cart, myCart ,checkout

class Cart_items(admin.ModelAdmin):
    list = ('user','ordered','total_price','product','price','total_items','quantity')

class ordered_ad(admin.ModelAdmin):
    list = ('user','email','name','address','phone')    

# admin.site.register(Cart,Cart_items)    
admin.site.register(myCart)
admin.site.register(checkout)