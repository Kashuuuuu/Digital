from django.contrib import admin
from signin.models import Profile

class Profile_admin(admin.ModelAdmin):
    list=('user','forgot_password_token')

admin.site.register(Profile)