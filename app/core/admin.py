from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext as _trans

from core import models

class UserAdmin(BaseUserAdmin):
    ordering = ['id']
    list_display = ['email', 'name']
    fieldsets = [
        ( None, {'fields': ('email', 'password')} ),
        ( _trans('Personal Info'), {'fields': ('name',)} ),
        (
            _trans('Permissions'), 
            { 'fields': ('is_active', 'is_staff', 'is_superuser') }
        ),
        ( _trans('Important Dates'), {'fields': ('last_login',)} )
    ]
    add_fieldsets = [
        (None, {
            'classes': ('wide', ),
            'fields': ('email', 'password1', 'password2')
        })
    ]


admin.site.register(models.User, UserAdmin)
admin.site.register(models.Tag)
admin.site.register(models.Ingredient)
