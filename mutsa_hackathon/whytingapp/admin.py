from django.contrib import admin
from .models import Store

class StoreAdmin(admin.ModelAdmin):
    model = Store
    def image(self, obj):
        return obj.image.image
    image.admin_order_field  = 'book__author'

    list_display = ['name', 'introduction', 'address', 'number', 'image' ]

admin.site.register(Store, StoreAdmin)