from django.contrib import admin
from .models import Profile, Owner, Customer
from django.contrib.auth.models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'password']
admin.site.unregister(User)    
admin.site.register(User, UserAdmin)

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'belong', 'number']
    list_filter = ['belong']
admin.site.register(Profile, ProfileAdmin)

class OwnerAdmin(admin.ModelAdmin):
    list_display = ['owner_id', 'id']
admin.site.register(Owner, OwnerAdmin)
admin.site.register(Customer)


