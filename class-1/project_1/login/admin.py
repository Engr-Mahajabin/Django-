from django.contrib import admin
from .models import User, Profile

# Register your models here.
class AdminUser(admin.ModelAdmin):
    list_display = ('email','is_staff','is_active')

class AdminProfile(admin.ModelAdmin):
    list_display = ['username','full_name','city','phone']
    list_editable = ['city']

admin.site.register(User, AdminUser)
admin.site.register(Profile, AdminProfile)