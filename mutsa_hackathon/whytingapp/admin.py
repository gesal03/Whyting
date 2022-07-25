from django.contrib import admin
from .models import Store, Image

class StoreAdmin(admin.ModelAdmin):
    model = Store
    def image(self, obj):
        return obj.image.all
    image.admin_order_field  = 'image'

    list_display = ['name', 'introduction', 'address', 'number', 'image' ]

admin.site.register(Store, StoreAdmin)
admin.site.register(Image)
