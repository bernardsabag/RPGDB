from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Character)
admin.site.register(Inventory)
admin.site.register(Item)

