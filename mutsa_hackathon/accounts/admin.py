from django.contrib import admin
from django.contrib.auth.models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ['get_name', 'username', 'get_belong', 'id', 'get_number']

    def get_name(self, obj):
        return obj.profile.name

    def get_belong(self, obj):
        return obj.profile.belong

    def get_number(self, obj):
        return obj.profile.number


admin.site.unregister(User)    
admin.site.register(User, UserAdmin)


