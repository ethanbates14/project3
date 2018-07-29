from django.contrib import admin

# Register your models here.
from .models import Categories, Menu, Prices

admin.site.register(Categories)
admin.site.register(Menu)
admin.site.register(Prices)