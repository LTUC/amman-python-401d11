from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username','first_name']
    # fieldsets= UserAdmin.fieldsets +(
    #     ('Contact Information',{
    #         'fields': ('phone_number',)
    #     }),
    # )
    fieldsets = (
        ('Auth Info', {
            'fields' : ('username','password','email')

        }),
        ('Personal Info',{
         'fields' : ('first_name','last_name')
        }),
        ('User permissions',{
            'fields':('is_staff','is_superuser')
        })
    )

admin.site.register(CustomUser, CustomUserAdmin)