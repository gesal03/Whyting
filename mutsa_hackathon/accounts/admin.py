from django.contrib import admin
from django.contrib.auth.models import User

class UserAdmin(admin.ModelAdmin):
    def number(self, obj):
        return obj.profile.number

    def name(self, obj):
        return obj.profile.name

    def belong(self, obj):
        return obj.profile.belong
    
    list_display = ['name', 'username', 'id', 'number', 'belong']
admin.site.unregister(User)    
admin.site.register(User, UserAdmin)



