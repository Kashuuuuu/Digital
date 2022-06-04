from django.contrib import admin

from dashboard.models import Slider,About,Services,Testimonial

# Register your models here.

    
class Slider_Admin(admin.ModelAdmin):
    list2 = ('slider_image','slider_text1','slider_text2')

class About_Admin(admin.ModelAdmin):
    list3 = ('icon','heading','description') 

class Services_Admin(admin.ModelAdmin):
    list3 = ('icon','heading','description') 

class Testimonial_Admin(admin.ModelAdmin):
    list3 = ('heading','image','description','subtext1','subtext2','icon1','icon2','icon3','icon4','icon5')           

admin.site.register(Slider,Slider_Admin)
admin.site.register(About,About_Admin)
admin.site.register(Services,Services_Admin)
admin.site.register(Testimonial,Testimonial_Admin)