from django.contrib import admin
from .models import Product,Profile, Rocket




# Register your models here.
admin.site.register(Product)
admin.site.register(Rocket)
admin.site.register(Profile)