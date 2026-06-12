from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

class CustomUserAdmin(UserAdmin):

    list_display = ['username', 'email']

    search_fields = ['username', 'email']

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('email',)}),
    )

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)