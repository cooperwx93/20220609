from django.contrib import admin
from .models import MyUser
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

# Register your models here.
@admin.register(MyUser)
class MyUserAdmin(UserAdmin):
    list_display = ['username', 'email', 'name', 'introduce',
                    'company', 'profession', 'address', 'telephone',
                    'wx', 'wb', 'qq', 'photo']
    fieldsets =  list(UserAdmin.fieldsets)
    fieldsets[1] = (_('Personal info'),
                    {'fields': ( 'email', 'name', 'introduce',
                    'company', 'profession', 'address', 'telephone',
                    'wx', 'wb', 'qq', 'photo')})
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(id=request.user.id)
