from django.contrib import admin
from .models import CustomUser
# Register your models here.
from django.contrib.auth.admin import UserAdmin

class CustomUserAdmin(UserAdmin):
    add_fieldsets = (
        ('None',{'fields' : ('username','email','password1', 'password2')}),
                     
        ('personal information',{'fields' :('first_name','last_name','phone_number') })

    )

admin.site.register(CustomUser,CustomUserAdmin)