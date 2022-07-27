from django.contrib import admin
from .models import Store, Image

class StoreAdmin(admin.ModelAdmin):
    list_display = ['name', 'address', 'number', 'waiting_state', 'id']

admin.site.register(Store, StoreAdmin)
admin.site.register(Image)

