from django.contrib import admin

# Register your models here.
from .models import Categories, Options,Menu,Topping,Prices

admin.site.register(Categories)
admin.site.register(Options)
admin.site.register(Topping)
admin.site.register(Menu)
admin.site.register(Prices)